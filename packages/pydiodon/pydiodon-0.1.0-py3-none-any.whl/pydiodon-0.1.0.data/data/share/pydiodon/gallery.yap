# demo for diosh

printc("\n#--------------------------------#", color="cyan")
printc("#                                #", color="cyan")
printc("#        demo for Diosh          #", color="cyan")
printc("#                                #", color="cyan")
printc("#--------------------------------#\n", color="cyan")

###
printc("\nHere are the operations permitting to run the gallery\n", color="cyan")
print("- creation of a directory called DIOSH_DEMO_DIR")
print("- changes the directory to this one")
print("- copy three files into it from the project:")
print("    - the source file gallery.yap with commands")
print("    - the yaml file with associated parameters")
print("    - the distance file chosen as an example: guiana_trees.sw.dis")

printc("\nIn what follows, diosh commands are in green, and comments in white\n", color="cyan")

### starting the session
printc("\n-> run gallery.yap", color="green")

input("press a key to continue")

### loading a distance file
printc("\n-> do load_mds_file", color="green")
print("Selecting a distance file for MDS")
print("file name is guiana_trees.sw.dis, given in yaml file")
do load_mds_file

### running a MDS
printc("\n-> do mds", color="green")
print("\nRunning a MDS, this may take a while ...")
do mds

### plotting components
printc("\n-> do plot_components_scatter", color="green")
print("\nPlotting components")
do plot_components_scatter

### plotting parallel coordinates
printc("\n-> do plot_components_splines", color="green")
print("\nPlotting parallel coordinates")
do plot_components_splines

### plotting eigenvalues
printc("\n-> do plot_eig", color="green")
print("\nPlotting eigenvalues")
do plot_eig
 
### computing quality
printc("\n-> do quality", color="green")
print("\nComputing quality of projection per item and axis")
do quality

### plotting quality per item
printc("\n-> do plot_components_quality per item", color="green")
print("\nPlotting quality of projection per item")
do plot_components_quality

### plotting quality per item
printc("\n-> do plot_quality", color="green")
print("\nPlotting quality of projection on one axis")
do plot_quality
