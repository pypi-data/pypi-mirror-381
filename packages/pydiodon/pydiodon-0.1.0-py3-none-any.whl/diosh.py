#!/usr/bin/env python3

import functools
import glob
import os
import re
import shutil
import subprocess
import multiprocessing
import sys
import traceback
import warnings
from datetime import datetime

import numpy as np
import yaml
from print_color import print as printc
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter, WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QFileDialog,
)
import pydiodon as _dio
_dio.__nprocs = set()
import diolib


def _init(y):
    compl = {}
    compl["do"] = {}
    compl["doc"] = {}
    compl["check"] = {}
    compl["?"] = {}
    compl["help"] = {}
    compl["set"] = {}
    compl["show"] = {}
    compl["run"] = {}
    compl["prompt on"] = None
    compl["prompt off"] = None
    compl["exit"] = None
    compl["quit"] = None
    compl["load yaml"] = None
    compl["create yaml"] = None
    compl["close plots"] = None

    func = set()
    # func.add("general")
    # func.add("mapping")

    with open(diolib.__file__, "r") as code:
        for l in code:
            if l.startswith("\tdef"):
                l = l.split()[1].split("(")[0]
                func.add(l)
    func.discard("__init__")

    for com in ("do", "check", "?", "help", "show", "set"):
        for f in sorted(func, key=lambda x: x.__repr__()):
            compl[com][f] = {}
            if f not in y.yam or y.yam[f] is None:
                y.yam[f] = {"_key": "_value"}

            if com == "set":
                for k in y.yam[f]:
                    compl[com][f][k] = None

    """
    del compl["do"]["__init__"]
    compl['set']['mapping'] = {}
    compl['set']['mapping']['reference'] = None
    compl['set']['mapping']['meth'] = None

    del compl["do"]["general"]
    del compl["do"]["mapping"]
    del compl["help"]["general"]
    del compl["help"]["mapping"]
    del compl["?"]["general"]
    del compl["?"]["mapping"]

    func.discard('general')
    func.discard('mapping')
    """
    compl['doc'] = compl["do"]
    do_compl = compl["do"]
    w_compl = WordCompleter(do_compl)
    for c in compl["do"]:
        compl["do"][c] = w_compl

    for s in glob.glob("*.yap"):
        compl["run"][s] = None

    completer = NestedCompleter.from_nested_dict(compl)

    histfile = os.environ["HOME"] + "/.dio_history"
    session = PromptSession(completer=completer, history=FileHistory(histfile))

    return func, session, completer

def _execute(args,_y):
    exec(args)


def _save(y, input_field):
    new_param = {}
    for section in input_field:
        new_param[section] = {}
        for i, it in enumerate(input_field[section].item):
            if isinstance(it, QLineEdit):
                v = it.text()
                if "." in v:
                    try:
                        v = float(v)
                    except ValueError:
                        pass
                else:
                    try:
                        v = int(v)
                    except ValueError:
                        pass
                if v == "False":
                    v = False
                    
                if v == "True":
                    v = True

            elif isinstance(it, QCheckBox):
                v = True if it.checkState() == Qt.Checked else False

            elif isinstance(it, QComboBox):
                v = it.currentText()

            new_param[section][input_field[section].name[i]] = v

    date = datetime.now().strftime("%d_%B_%Y_%H:%M:%S")
    oldYaml = f"{y.configfile}.old"
    os.rename(y.configfile, oldYaml)

    for s in new_param:
        for v in new_param[s]:
            y.yam[s][v] = new_param[s][v]

    with open(y.configfile, "w") as y_out:
        print("#", "-" * 40, file=y_out)
        print("#      Configuration file\n#\n#", "-" * 40, "\n#", file=y_out)
        print(f"# {date}\n#\n#", "-" * 40, "\n", file=y_out)

        """    
        #general first
        print("general:", file=y_out)
        for v in y.yam["general"]:
            if v == 'None': v=''
            print(f'  {v}: {y.yam["general"][v]}', file=y_out)
        """

        for k in sorted(y.yam):
            if k == "__Run_OK__": # or k == "general" or "_key" in y.yam[k]:
                continue
            print("\n#", "-" * 40, file=y_out)
            print(f"{k}:", file=y_out)

            for v in y.yam[k]:
                '''
                if v == "None" or v == '':
                    v = "False"
                '''
                if v == '_key': continue
                print(f"  {v}: {y.yam[k][v]}", file=y_out)

    printc(f"{y.configfile} updated", color="magenta")


def _fileSelect(btn, _):
    filename, ok = QFileDialog.getOpenFileName()
    if os.path.dirname(filename) == os.getcwd():
        filename = os.path.basename(filename)
    btn.setText(filename)

def _check(y, module, meth, run_bt=True):
    f = getattr(module, meth)
    filename = f.__code__.co_filename
    start = f.__code__.co_firstlineno
    end = [l for l in f.__code__.co_lines()][-1][-1]
    params = {meth: [], "general": [], "mapping": []}
    param_list = []
    with open(filename, "r") as code:
        for i, l in enumerate(code):
            if i < start:
                continue
            if i > end:
                  break
            m = re.search(rf"self.yam\[(\w+)]\[['\"](\w+)['\"]\]", l)

            if m:
                section = meth if m.groups()[0] == "f_name" else m.groups()[0]
                if section not in params:
                    params[section] = []
                param_list.append(m.groups()[1])
                params[section].append(m.groups()[1])
                y.yam["__Run_OK__"] = "OK"

    # No params
    if len(param_list) == 0:
        y.yam["__Run_OK__"] = "OK"
        print(f"No parameters for {meth}")
        return

    input_field = {}
    metLayout = QFormLayout()
    metLayout.section = meth
    metQframe = QFrame()
    metQframe.setLineWidth(3)
    metQframe.setMidLineWidth(0)
    metQL = QLabel(f"{meth} parameters:")
    metQL.setAlignment(Qt.AlignCenter)
    metQframe.setLayout(metLayout)
    qvBoxLayout = QVBoxLayout()

    # Add "General parameters"
    if params["general"]:
        input_field["general"] = genLayout(qvBoxLayout, y, params, meth)

    # Add "Mapping" parameters
    if params["mapping"]:
        input_field["mapping"] = mapLayout(qvBoxLayout, y, params)

    qvBoxLayout.addWidget(metQL)
    qvBoxLayout.addWidget(metQframe)

    metLayout.item = []
    metLayout.name = params[meth]

    for p in params[meth]:
        pText = ""
        if p in y.yam[meth]:
            pText = str(y.yam[meth][p])
        if p in _rc["bool"]:
            metLayout.item.append(QCheckBox())
            if pText in ("True", "true", "Yes", "yes"):
                metLayout.item[-1].setCheckState(Qt.Checked)
        elif p in _rc["list"]:
            metLayout.item.append(QComboBox())
            metLayout.item[-1].addItems([pText] + _rc["list"][p])
            if p == "varname":
                klist = [pText]
                klist += np.loadtxt(y.charfile, delimiter="\t", dtype=str, max_rows=1)[
                    1:
                ].tolist()
                metLayout.item[-1].addItems(klist)
        elif 'file' in p: #p.endswith('file'):
            fText = QLineEdit(pText)
            fText.setFixedWidth(500)
            metLayout.item.append(fText)
            metLayout.addRow(f"{p}", metLayout.item[-1])
            p = ""
            metLayout.item.append(QPushButton(f"Change {p} ..."))
            metLayout.item[-1].clicked.connect(functools.partial(_fileSelect, fText))
        else:
            if pText == "None":
                pText = ""
            metLayout.item.append(QLineEdit(pText))

        metLayout.addRow(f"{p}", metLayout.item[-1])
    input_field[meth] = metLayout

    window = QDialog()
    window.setWindowTitle(meth)

    exit_bt = QPushButton("Exit")
    exit_bt.setShortcut(QKeySequence("Ctrl+E"))
    exit_bt.clicked.connect(window.reject)
    qvBoxLayout.addWidget(exit_bt)

    save_bt = QPushButton("Save")
    save_bt.setShortcut(QKeySequence("Ctrl+S"))

    for i, it in enumerate(input_field[section].item):
        if isinstance(it, QPushButton):
            del input_field[section].item[i]
            i = i - 1

    save_bt.clicked.connect(functools.partial(_save, y, input_field))
    qvBoxLayout.addWidget(save_bt)

    if run_bt:
        run_bt = QPushButton("Run")
        run_bt.clicked.connect(window.accept)
        run_bt.setShortcut(QKeySequence("Ctrl+R"))
        run_bt.setShortcut(QKeySequence("Return"))
        qvBoxLayout.addWidget(run_bt)

    window.setLayout(qvBoxLayout)

    res = window.exec()

    if res == QDialog.Rejected:
        window.close()
        y.yam["__Run_OK__"] = "NO"

    if res == QDialog.Accepted:
        y.yam["__Run_OK__"] = "OK"
        window.close()

    for section in input_field:
        for i, it in enumerate(input_field[section].item):
            if isinstance(it, QLineEdit):
                v = it.text()
                if "." in v:
                    try:
                        v = float(v)
                    except ValueError:
                        pass
                else:
                    try:
                        v = int(v)
                    except ValueError:
                        pass
                if v in ("False", "None", "No", "N"):
                    v = False
                if v in ("True", "Yes", "Y"):
                    v = True

            elif isinstance(it, QCheckBox):
                v = True if it.checkState() == Qt.Checked else False

            elif isinstance(it, QComboBox):
                v = it.currentText()

            if v == "":
                printc(
                    f"{input_field[section].name[i]}: {param_list[i]} missing",
                    tag="Warning",
                    tag_color="red",
                    format="bold",
                    color="cyan",
                )
                y.yam["__Run_OK__"] = "Missing arguments"
            else:
                y.yam[section][input_field[section].name[i]] = v


def _create_yaml(y, basename):

    print(f'{y=} {basename=}')



    params = {}
    meth = None
    with open(diolib.__file__, "r") as code:
        for i, l in enumerate(code):
            if l.startswith("\tdef"):
                f = re.search(r"def (\w+)", l)
                meth = f.groups()[0]
                params[meth] = set()
            m = re.search(rf"self.yam\[(\w+)\]\[['\"](\w+)['\"]\]", l)
            if m:
                sec, arg = m.groups()
                if sec == "f_name":
                    sec = meth
                params[sec].add(arg)

    f = y.__init__
    filename = f.__code__.co_filename
    in_class = False
    with open(filename, "r") as code:
        for i, l in enumerate(code):
            if l.startswith("class"):
                in_class = True
            if not in_class:
                continue
            if l.startswith("\tdef"):
                f = re.search(r"\tdef (\w+)", l)
                meth = f.groups()[0]
                params[meth] = set()

            m = re.search(rf"self.yam\[(\w+)\]\[['\"](\w+)['\"]\]", l)
            if m:
                sec, arg = m.groups()
                if sec == "f_name":
                    sec = meth
                params[sec].add(arg)
    params["__init__"].add("if_questions")

    date = datetime.now().strftime("%d %b %Y %H:%M:%S")
    if os.path.exists(f"{basename}.yaml"):
        oldYaml = f"{y.configfile}.old"
        os.rename(y.configfile, oldYaml)

    with open(f"{basename}.yaml", "w") as yf:
        print("#", "-" * 40, file=yf)
        print("#      Configuration file\n#\n#", "-" * 40, "\n#", file=yf)
        print(f"# {date}\n#\n#", "-" * 40, "\n", file=yf)

        # __init__
        print(f"__init__:\n  if_questions:  True", file=yf)
        print("\n#", "-" * 40, file=yf)

        for m in sorted(params):
            if m in ("general", "__init__"):
                continue
            print(f"{m}:", file=yf)
            for l in sorted(params[m]):
                if m in y.yam and l in y.yam[m]:
                    print(f"  {l}:  {y.yam[m][l]}", file=yf)
                else:
                    print(f"  {l}:", file=yf)
            print("\n#", "-" * 40, file=yf)

            ################################
            #                              #
            #             Main             #
            #                              #
            ################################


def main():
    _YAPSH_HELP = """
Usage:\tdiosh [-h]\n\tdiosh basename [script.yap]\n\tdiosh gallery

After the prompt: dio:[projectname]->
\tHit <TAB> for a list of available commands (autocompletion)
\ttype ! and a shell command
\ttype a python instruction
"""
    try:
        _basename = sys.argv[1]
    except IndexError:
        sys.exit(_YAPSH_HELP)

    if _basename == "-h":
        sys.exit(_YAPSH_HELP)

    if _basename == 'gallery':
        datadir = os.path.dirname(__file__)
        #Installation with pip install -e .
        if datadir.endswith('src'):
            datadir = f'{datadir[:-4]}/gallery'
        #installation with pip install . or pip3 install git+https
        else:
            datadir = f'{os.environ["HOME"]}/.local/share/pydiodon'

        shutil.rmtree('DIOSH_DEMO_DIR', ignore_errors=True)
        os.makedirs('DIOSH_DEMO_DIR')
        os.chdir('DIOSH_DEMO_DIR')
        for f in glob.glob(f'{datadir}/*'):
            shutil.copy2(f, '.')
        sys.argv.append('gallery.yap')

        '''
        elif demo == "malabar":
            os.makedirs(f'{os.environ["HOME"]}/.local/share/yap', exist_ok=True)
            os.chdir(f'{os.environ["HOME"]}/.local/share/yap')
            _basename = "190204_BM_Ben_Tey_B_rbcL"
            if not os.path.exists("190204_BM_Ben_Tey_B_rbcL.sw.h5"):
                os.system(
                    "wget https://entrepot.recherche.data.gouv.fr/api/access/datafile/148489 --output-document=190204_BM_Ben_Tey_B_rbcL.h5"
                )
                os.rename("190204_BM_Ben_Tey_B_rbcL.h5", "190204_BM_Ben_Tey_B_rbcL.sw.h5")
        else:
            sys.exit(_YAPSH_HELP)
    else:
     _yamls = glob.glob("*.yaml")
        '''
   
    if len(glob.glob("*.yaml")) > 1:
        printc(
            "\nMany Yaml files in this directory !",
            tag="!! WARNING !!",
            tag_color="red",
            format="bold",
            color="cyan",
        )
    
    if f"{_basename}.yaml" not in glob.glob("*.yaml"):
        printc(
            f"{_basename}.yaml does not exist. Should I create it ? (y/n) ",
            color="green",
        )
        if input().lower() in ("y", "yes"):
            _y = diolib.diodsl(_basename)
            _create_yaml(_y, _basename)
            print(f"{_basename}.yaml created")
        else:
            sys.exit()

    _y = diolib.diodsl(_basename)
    module = diolib.diodsl
    _app = QApplication([])

    if not _y.yam:
        _y.yam = {}
    func, session, completer = _init(_y)

    _script = False
    cmds = []
    #_scriptfile = "command"

    style = Style.from_dict(
        {
            "prompt": "red",
        }
    )
    message = [("class:prompt", f"dio:{_basename}-> ")]
    _pr = "on"

    # diosh basename script.yap
    if len(sys.argv) == 3:
        _script = True
        cmds = [""]
        _script_line = 0
    
    DOC_BASE_URL = 'https://diodon.gitlabpages.inria.fr/pydiodon'

    while True:
        if _script:
            if len(cmds) == 0:
                _script = False
                continue
            rep = cmds.pop(0)
            rep = rep.lstrip(" ")
            rep = rep.rstrip('\n')
            _script_line += 1
        else:
            try:
                rep = session.prompt(message, style=style, completer=completer)
            except (EOFError, KeyboardInterrupt):
                os._exit(0) # Ctrl-d, Ctrl-c: garde les plots
        if rep in ("exit", "quit", "quit()", "q()"):
            #ferme  les plots
            for p in _dio._procs:
                p.terminate()
            break

        if len(sys.argv) == 3:
            rep = f"run {sys.argv.pop()}"

        if rep == "":
            continue

        if rep == "help" or rep == "?":
            print(_YAPSH_HELP)
            continue

        if rep == "run":
            continue

        if rep.startswith("run "):
            _scriptfile = rep.split("run ")[1]
            if not _scriptfile:
                continue
            _script = True
            _script_line = 0
            try:
                with open(_scriptfile, "r") as scr:
                    cmds = scr.readlines()
            except FileNotFoundError:
                printc(f"{_scriptfile} not found", color="cyan")
            continue

        if ";" in rep:
            _script = True
            _script_line = 0
            cmds = rep.split(";")
            continue

        if rep == "do":
            for m in sorted(func):
                print(m)
            print()
            continue

        if rep.startswith("do "):
            methods = rep.split()[1:]
            exit_loop = False
            for m in methods:
                if m not in func:
                    printc(f"\n !!! Method {m} unknown !!\n", color="red")
                    exit_loop = True
                    break
            if exit_loop:
                continue

            for m in methods:
                if _y.yam["__init__"]["if_questions"]:
                    _check(_y, module, m)
                else:
                    _y.yam["__Run_OK__"] = "OK"

                if "__Run_OK__" in _y.yam and _y.yam["__Run_OK__"] == "OK":
                    try:
                        '''
                        #https://stackoverflow.com/questions/458209/is-there-a-way-to-detach-matplotlib-plots-so-that-the-computation-can-continue/56982302#56982302
                        #!! multiprocessing.Process.... n'assigne pas les attributs
                        if m.startswith('plot'):    
                            multiprocessing.Process(target=_execute, args=(f"diolib.diodsl.{m}(_y)",_y), daemon=True).start()
                        else:
                        '''
                        getattr(module,m)(_y)
                    except Exception as e:
                        if "DEBUG" in os.environ:
                            traceback.print_exc()
                        else:
                            print(e, end=" ")
                        if _script:
                            print(f"in {_scriptfile} line {_script_line}", end=" ")
                            _script = False
                        print()
            continue
        
        if rep == 'close plots':
            #ferme  les plots
            for p in _dio.__nprocs:
                p.terminate()
            continue


        if rep == "check":
            continue

        if rep.startswith("check "):
            m = rep.split()[1]
            # if  m != 'general' and  m != 'mapping' and m not in func:
            if m not in func:
                printc(f"\n !!! Method {m} unknown !!\n", color="red")
                continue

            try:
                #getattr(module, m)
                _check(_y, module, m, run_bt=False)
            except AttributeError as e:
                if "DEBUG" in os.environ:
                    traceback.print_exc()
                continue
            continue

        if rep == "show":
            for k in _y.yam:
                if isinstance(_y.yam[k], dict):
                    print(f"{k}:")
                    for l in _y.yam[k]:
                        print(f"\t{l}:\t{_y.yam[k][l]}")
                else:
                    print(f"{k}:\t\t{_y.yam[k]}")
            print()
            continue

        if rep.startswith("show "):
            r = rep.split()
            if r == ["show"]:
                continue
            try:
                _y.yam[r[1]]
            except KeyError:
                continue

            if isinstance(_y.yam[r[1]], dict):
                print(f"{r[1]}:")
                for k in _y.yam[r[1]]:
                    try:
                        if r[2] in k:
                            print(f"\t{k}: {_y.yam[r[1]][k]}")
                    except IndexError:
                        print(f"\t{k}: {_y.yam[r[1]][k]}")
            continue

        if rep.startswith("set "):
            r = rep.split()
            if r == ["set"]:
                continue
            if not r[1] in _y.yam:
                continue

            if isinstance(_y.yam[r[1]], dict):
                if len(r) == 2:
                    for k in _y.yam[r[1]]:
                        print(f"{k}:\t{_y.yam[r[1]][k]}")

                elif len(r) == 3:
                    print(f"{r[1]}:\t{r[2]}:  ", end="")
                    if r[2] in _y.yam[r[1]]:
                        print(f"{_y.yam[r[1]][r[2]]}")
                    else:
                        print("None")

                elif len(r) == 4:
                    if r[3] in ("True", "true" "yes", "Yes"):
                        r[3] = True
                    elif r[3] in ("False", "false", "no", "No"):
                        r[3] = False
                    _y.yam[r[1]][r[2]] = r[3]
                    print(f"{r[1]}:\t{r[2]}: {r[3]}")
                else:
                    print(f"Too much parameters ({len(r)}) for setting")
                continue

            else:
                if len(r) == 2:
                    print(f"{r[1]}:\t{_y.yam[r[1]]}")

                elif len(r) == 3:
                    if r[2] in ("True", "true" "yes", "Yes"):
                        r[2] = True
                    elif r[2] in ("False", "false", "no", "No"):
                        r[2] = False
                    _y.yam[r[1]] = r[2]
                    print(f"{r[1]}:\t{r[2]}")
            continue

        if rep.startswith("prompt "):
            _pr = rep.split("prompt ")[1]
            if not _pr in ("on", "off"):
                continue
            if _pr == "on":
                message = [("class:prompt", f"dio:{_basename}-> ")]
            else:
                message = [("class:prompt", f"dio-> ")]
            continue

        if rep.startswith("? ") or rep.startswith("help "):
            r = rep.split()[1]
            try:
                f = getattr(diolib.diodsl, r)
                print(f.__doc__)
            except (AttributeError, IndexError):
                continue
            continue

        if rep.startswith("!"):
            try:
                subprocess.run(
                    [rep[1:]], shell=True, check=True, executable="/bin/bash"
                )
            except Exception as e:
                traceback.print_exc()
                pass

            continue

        if rep == 'doc':
            os.system(f'xdg-open {DOC_BASE_URL}')
            continue

        if rep.startswith('doc '):
            m = rep.split()[1]
            m = 'load_ascii' if m == 'load_file' else m 
            os.system(f'xdg-open {DOC_BASE_URL}/fonctions/pydiodon.{m}.html')
            continue
            


        if rep == "load yaml":
            try:
                _y.yam.update(yaml.load(open(_y.configfile), Loader=yaml.SafeLoader))
                print(f"[dio!]: {_y.configfile} loaded")
            except Exception as e:
                traceback.print_exc()

            _y = diolib.diodsl(_basename)
            func, session, completer = _init(_y)
            continue

        if rep == "create yaml":
            _create_yaml(_y, _basename)
            printc(f"{_y.configfile} created (old one saved as {_y.configfile}.old)", color="green")
            continue

        if rep == "switch":
            continue

        if rep.startswith("switch "):
            dirname = rep.split("switch ")[1]
            curr_dir = os.getcwd()
            try:
                os.chdir(dirname)
            except FileNotFoundError:
                print(f"directory {dirname} not found")
                continue
            try:
                _basename = glob.glob("*.yaml")[0][:-5]
            except IndexError:
                print(f"No yaml file in {dirname}")
                os.chdir(curr_dir)
                continue

            _pr = "on"
            message = [("class:prompt", f"dio:{_basename}-> ")]
            _y = diolib.diodsl(_basename)
            if not _y.yam:
                _y.yam = {}
            func, session, completer = _init(_y)
            continue

        try:
            exec(rep)
        except Exception as e:
            if "DEBUG" in os.environ:
                traceback.print_exc()
            else:
                print(f"{e}", end=" ")
            if _script:
                print(f"in {_scriptfile} line {_script_line}", end=" ")
                _script = False
            print()
            continue


_rc = {
    "list": {
        "coord": ["mds", "tsne"],
        "dis_algo": ["sw", "nw"],
        "dis_type": ["dis", "h5"],
        "otype": ["tsv"],
        "fmt": ["png", "eps", "pdf", "ascii"],
        "suffix": ['.txt','.csv', '.gz', '.bz2'],
        "otu_meth": ["cc", "hac", "islands", "swarm"],
        "varname": [],
        "meth": ["svd", "evd", "grp"],
        "color_range": ["discrete", "continuous"],
        "initialisation": ["fasta", "fastq", "h5"],
        "mode": ["2cols", "df"],
    },
    "bool": [
        "if_questions",
        "save",
        "x11",
        "load_h5",
        "kde",
        "colorfile",
    ],
}


if __name__ == "__main__":
    main()

