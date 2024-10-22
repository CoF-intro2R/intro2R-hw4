
import pytest
import os

# check dir structure first
def test_dir_struc():
  assert os.path.isdir("R")
  assert os.path.isfile("R/hw4.R")
  assert os.path.isfile("R/data_cleaning.R")
  assert os.path.isdir("Figures")
  assert os.path.isfile("Figures/num_captures_hja_verts.png")
  assert os.path.isfile("Figures/mean_mass_hja_verts.png")

