#!/usr/bin/env julia

using Match
using DelimitedFiles
using Statistics
using LinearAlgebra

function center_col(A::Matrix{Float64})
  m  = mean(A,dims=1)
  Ac = A .- m
  return Ac, m
end


function pca_svd(A::Matrix{Float64})
  U,S,VT = svd(A)
  V			 = transpose(VT)
  Y      = U  * Diagonal(S)
  L      = S .* S
  return Y, L, V
end

function pca_core(A::Matrix{Float64}; k::Int=-1, meth::String="evd")
  Y = L = V = 0
  @match meth begin
    "evd" => println("evd Not yet implemented")
    "svd" =>  begin;
          Y, L, V = pca_svd(A);
              end;
    "grp" => begin;
          if k == -1
            println("in pca_grp(), a value for k must be given explicitly")
          end
          println("grp Not yet implemented")
          end
        _     => println("Meth ???", meth)
  end

  if k > 0 && meth in ["evd", "svd"]
    Y = Y[:,1:k]
    L = L[1:k]
    V = V[:,1:k]
  end
  return Y, L, V
end

function pca(A::Matrix{Float64};pretreatment="standard", k=-1, meth="evd", correlmat=true)
  m,n  = size(A)
  # transposition if necessary
  if n > m
    transpose!(A)
    transpose_flag::Bool = true
  else
    transpose_flag = false
  end

  # no correlation matrix if grp method
  if meth=="grp"
		correlmat = false
  end
  
  accepted = ["standard","bicentering", "scaling", "col_centering", "row_centering"]
  if !(pretreatment in accepted)
    println("required pretreatment $pretreatment is not recognized. Accepted strings are")
		println(accepted)
  end
#=
  @match pretreatment begin
    "standard" => 
    =#
end

infileName = ARGS[1]
M = readdlm(infileName)
#=
Y, L, V = pca_core(M; meth="svd", k=5)
println(Y)
println(center_col(M))

pca(M, pretreatment="toto")
=#



