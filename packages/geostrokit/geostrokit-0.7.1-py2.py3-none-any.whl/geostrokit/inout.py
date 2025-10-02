#!/usr/bin/env python

import numpy as np
from scipy.io import netcdf_file

from .grid import *

def write_bas(fname, psi):
  """
  Write basilisk format output

  Parameters
  ----------

  psi : array [(nz,) ny,nx]
  fname: file name

  Returns
  -------

  nothing
  """

  nd = psi.ndim

  if nd == 1:
    print("not handeling 1d arrays")
    sys.exit(1)
  elif nd == 2:
    psi = psi[None,:,:]

  nl,N,naux = psi.shape

  # combine and output in .bas format: (z,x,y)
  p_out = np.zeros((nl,N+1,N+1))
  p_out[:,0,0] = N
  p_out[:,1:,1:] = psi
  p_out = np.transpose(p_out,(0,2,1))
  p_out.astype('f4').tofile(fname)


def read_bas(fname):
  """
  Read basilisk format file

  Parameters
  ----------

  fname: file name

  Returns
  -------

  psi : array [(nz,) ny,nx]
  """

  psi  = np.fromfile(fname,'f4')
  N = int(psi[0])
  N1 = N + 1
  nl = int(len(psi)/N1**2)

  psi  = psi.reshape(nl,N+1,N+1).transpose(0,2,1)[:,1:,1:]

  return psi.squeeze()


def read_nc(fname, it, var='p', rescale=1.0, interp=False, subtract_bc=False):
  """
  Read a variable from a NetCDF file, with optional rescaling, interpolation,
  and boundary condition subtraction.

  Parameters
  ----------
  fname : str
      Path to the NetCDF file to read.
  
  it : int
      Time index (iteration) to read in the file.
  
  var : str, optional
      Name of the variable to read from the NetCDF file. Default is 'p'.
  
  rescale : float, optional
      Factor to multiply the output data by. Default is 1.0.
  
  interp : bool, optional
      If True, interpolate the variable data from cell nodes to cell centers. Default is False.
  
  subtract_bc : bool, optional
      If True, subtracts the value at the lower-left corner (first index of each dimension)
      from the entire array (i.e., removes a baseline). Useful for removing constant boundary conditions.
      Default is False.

  Returns
  -------
  psi : ndarray
      The extracted data array, typically 3D ([z, y, x]), possibly rescaled, 
      interpolated, and/or baseline-subtracted.

  Notes
  -----
  - This function assumes the variable has a time dimension as its first axis.

  Example
  -------
  >>> psi = read_nc('ocean_data.nc', it=0, var='temperature', rescale=0.001, interp=True)
  >>> print(psi.shape)
  (10, 49, 99)  # assuming original was (10, 50, 100) and interp reduces grid size by 1
  """

  f = netcdf_file(fname,'r')
  psi = f.variables[var][it,...].copy()
  f.close()

  if subtract_bc:
    psi = psi - psi[:,0,0][:,None,None]

  psi *= rescale

  if interp:
    psi = interp_on_c(psi)

  return psi


def write_nc(fname, var, timeDim = False):
  """
  Write a NetCDF file from a dictionary of 2D or 3D NumPy arrays.

  Parameters
  ----------
  fname : str
      Name of the NetCDF file to create (including path if necessary).
  
  var : dict
      Dictionary of variables to write to the file. Each value should be a NumPy array 
      (2D or 3D). Keys will be used as variable names in the NetCDF file.
  
  timeDim : bool, optional
      If True, adds an unlimited time dimension ('t') and writes variables 
      as if they have a leading time axis. Default is False.

  Returns
  -------
  None
      The function writes the specified data to a NetCDF file and does not return any value.

  Example
  -------
  >>> import numpy as np
  >>> import geostrokit as qg
  >>> data = {
  ...     'temperature': np.random.rand(10, 50, 100),  # 3D: z, y, x
  ...     'salinity': np.random.rand(10, 50, 100)
  ... }
  >>> qg.write_nc('ocean_data.nc', data, timeDim=True)
  """

  f = netcdf_file(fname,'w')

  ndmax = 0
  for key, psi in var.items():
    nd = psi.ndim
    ndmax = np.max((nd,ndmax))
    if nd == ndmax:
      si = psi.shape

  nd0 = 0
  if timeDim:
    f.createDimension('t',None)
  if ndmax > 2:
    f.createDimension('z',si[0])
    nd0 += 1
  f.createDimension('y',si[nd0])
  f.createDimension('x',si[nd0+1])

  alldims_2d = ()
  alldims_3d = ()
  if timeDim:
    tpo = f.createVariable('t', 'f', ('t',))
    alldims_2d += ('t',)
    alldims_3d += ('t',)
  if ndmax > 2:
    zpo = f.createVariable('z', 'f', ('z',))
    alldims_3d += ('z',)
  ypo = f.createVariable('y', 'f', ('y',))
  xpo = f.createVariable('x', 'f', ('x',))
  alldims_2d += ('y', 'x',)
  alldims_3d += ('y', 'x',)

  varout = {}
  for key, psi in var.items():
    nd = psi.ndim
    if nd > 2:
      varout[key] = f.createVariable(key , 'f', alldims_3d)
    else:
      varout[key] = f.createVariable(key , 'f', alldims_2d)

  if ndmax > 2:
    zpo[:] = np.arange(si[0])
  ypo[:] = np.arange(si[nd0])
  xpo[:] = np.arange(si[nd0+1])

  for key, psi in var.items():
    if timeDim:
      varout[key][0] = psi
      tpo[0] = 0
    else:
      varout[key][:] = psi

  f.close()


def read_time(pfiles):
  """
  Check number of time steps

  Parameters
  ----------

  pfiles : list of pressure files

  Returns
  -------

  si_t : int, total number of timestep
  """

  if pfiles[0][-4:] == '.bas':
    si_t = len(pfiles)
  else:
    f = netcdf_file(pfiles[0],'r')
    time = f.variables['time'][:].copy()
    f.close()
    si_t = int(len(time)*len(pfiles))
  return si_t


def load_generic(pfiles, it, var='p', rescale=1, interp=False, si_t=1, subtract_bc=False):
  """
  Generic load function for list of files

  Parameters
  ----------

  pfiles : list of pressure files
  it: int iteration number
  var: str, variable name (optional)
  rescale: float, multiply output by rescale factor
  interp: Bool, interpolate on grid center (default: False)
  si_t: int, total length of data set
  subtract_bc: Bool, subtract bc (default: False)

  Returns
  -------

  psi : array [nz, ny,nx]
  """

  if pfiles[0][-4:] == '.bas':
    p = read_bas(pfiles[it])
  else:
    it_per_file = int(si_t/len(pfiles))
    ifi = int(it/it_per_file)
    it1 = int(it - ifi*it_per_file)
    p = read_nc(pfiles[ifi], it1, var, rescale, interp, subtract_bc)

  return p
