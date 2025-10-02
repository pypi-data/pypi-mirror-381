"""

3d elliptic solver based on 

2017 A. R. Malipeddi
A simple 2D geometric multigrid solver for the homogeneous Dirichlet Poisson problem on Cartesian grids and unit square. Cell centered 5-point finite difference operator.
https://github.com/AbhilashReddyM/GeometricMultigrid/


"""

import numpy as np
from scipy.sparse.linalg import LinearOperator
from scipy.linalg import solve_banded

from .grid import *
from .pv import *

def Jacrelax_2d(level,u,f, L0, Smat, f_type, mask, iters=1,pre=False):
  '''
  under-relaxed Jacobi method smoothing
  '''

  si = u.shape
  nx = (si[-1]-2)
  ny = (si[-2]-2)

  if f_type == 'center': # centered field
    dx = L0/nx # L0 is the last dimension
    dy = dx
  else: # nodal field
    dx = L0/(nx+1)
    dy = dx

  Ax = 1.0/dx**2; Ay = 1.0/dy**2
  Ap = 1.0/(2.0*(Ax+Ay))

  if isinstance(mask,np.ndarray):
    mask = mask[:,1:ny+1,1:nx+1]

  #Dirichlet BC
  if f_type == 'center': # centered field
    u[:, 0,:] = -u[:, 1,:]
    u[:,-1,:] = -u[:,-2,:]
    u[:,:, 0] = -u[:,:, 1]
    u[:,:,-1] = -u[:,:,-2]
  else: # nodal field
    u[:, 0,:] = 0.
    u[:,-1,:] = 0.
    u[:,:, 0] = 0.
    u[:,:,-1] = 0.

  #if it is a pre-sweep, u is fully zero (on the finest grid depends on BC, always true on coarse grids)
  # we can save some calculation, if doing only one iteration, which is typically the case.
  if(pre and level>1):
    u[:,1:ny+1,1:nx+1] = -Ap*f[:,1:ny+1,1:nx+1]*mask
    #Dirichlet BC
    if f_type == 'center': # centered field
      u[:, 0,:] = -u[:, 1,:]
      u[:,-1,:] = -u[:,-2,:]
      u[:,:, 0] = -u[:,:, 1]
      u[:,:,-1] = -u[:,:,-2]
    else:  # nodal field
      u[:, 0,:] = 0.
      u[:,-1,:] = 0.
      u[:,:, 0] = 0.
      u[:,:,-1] = 0.

    iters = iters - 1

  for it in range(iters):
    u[:,1:ny+1,1:nx+1] = Ap*(Ay*(u[:,2:ny+2,1:nx+1] + u[:,0:ny,1:nx+1])
                         + Ax*(u[:,1:ny+1,2:nx+2] + u[:,1:ny+1,0:nx])
                         - f[:,1:ny+1,1:nx+1])*mask
    #Dirichlet BC
    if f_type == 'center': # centered field
      u[:, 0,:] = -u[:, 1,:]
      u[:,-1,:] = -u[:,-2,:]
      u[:,:, 0] = -u[:,:, 1]
      u[:,:,-1] = -u[:,:,-2]
    else: # nodal field
      u[:, 0,:] = 0.
      u[:,-1,:] = 0.
      u[:,:, 0] = 0.
      u[:,:,-1] = 0.

#  if(not pre):
#    return u,None

  res = np.zeros_like(u)
  res[:,1:ny+1,1:nx+1] = (f[:,1:ny+1,1:nx+1]-(( Ay*(u[:,2:ny+2,1:nx+1]+u[:,0:ny,1:nx+1])
                                       + Ax*(u[:,1:ny+1,2:nx+2]+u[:,1:ny+1,0:nx])
                                       - 2.0*(Ax+Ay)*u[:,1:ny+1,1:nx+1])))*mask
  return u,res


def Jacrelax_3d(level,u,f, L0, Smat, f_type, mask, iters=1,pre=False):
  '''
  under-relaxed Jacobi method smoothing
  '''

  si = u.shape
  nx = (si[-1]-2)
  ny = (si[-2]-2)
  nl = si[0]

  Sl = np.copy(Smat)

  if f_type == 'center': # centered field
    dx = L0/nx 
    dy = dx
  else: # nodal field
    dx = L0/(nx+1)
    dy = dx

  Ax = 1.0/dx**2; Ay = 1.0/dy**2
  Ap = 1.0/(2.0*(Ax+Ay))
  iAp = 2.0*(Ax+Ay)
  Sl[1,:,:,:] -= iAp

  if isinstance(mask,np.ndarray):
    mask = mask[:,1:ny+1,1:nx+1]
  #Dirichlet BC
  if f_type == 'center': # centered field
    u[:, 0,:] = -u[:, 1,:]
    u[:,-1,:] = -u[:,-2,:]
    u[:,:, 0] = -u[:,:, 1]
    u[:,:,-1] = -u[:,:,-2]
  else: # nodal field
    u[:, 0,:] = 0.
    u[:,-1,:] = 0.
    u[:,:, 0] = 0.
    u[:,:,-1] = 0.

  #if it is a pre-sweep, u is fully zero (on the finest grid depends on BC, always true on coarse grids)
  # we can save some calculation, if doing only one iteration, which is typically the case.
  if(pre and level>1):
    u[:,1:ny+1,1:nx+1] = f[:,1:ny+1,1:nx+1]/Sl[1,:,:,:]*mask
    #Dirichlet BC
    if f_type == 'center': # centered field
      u[:, 0,:] = -u[:, 1,:]
      u[:,-1,:] = -u[:,-2,:]
      u[:,:, 0] = -u[:,:, 1]
      u[:,:,-1] = -u[:,:,-2]
    else: # nodal field
      u[:, 0,:] = 0.
      u[:,-1,:] = 0.
      u[:,:, 0] = 0.
      u[:,:,-1] = 0.

    iters=iters-1

  for it in range(iters):
    rhs = f[:,1:ny+1,1:nx+1] - (Ay*(u[:,2:ny+2,1:nx+1] + u[:,0:ny,1:nx+1])
                                + Ax*(u[:,1:ny+1,2:nx+2] + u[:,1:ny+1,0:nx]))

    #replace by thomas algorithm?
    u[:,1:ny+1,1:nx+1] = np.reshape(solve_banded((1,1), Sl[:,:,0,0], np.reshape(rhs,(nl,ny*nx))),(nl,ny,nx))*mask

    #Dirichlet BC
    if f_type == 'center': # centered field
      u[:, 0,:] = -u[:, 1,:]
      u[:,-1,:] = -u[:,-2,:]
      u[:,:, 0] = -u[:,:, 1]
      u[:,:,-1] = -u[:,:,-2]
    else: # nodal field
      u[:, 0,:] = 0.
      u[:,-1,:] = 0.
      u[:,:, 0] = 0.
      u[:,:,-1] = 0.

#  if(not pre):
#    return u,None

  res=np.zeros_like(u)
  res[:,1:ny+1,1:nx+1]=(f[:,1:ny+1,1:nx+1]-( Ay*(u[:,2:ny+2,1:nx+1]+u[:,0:ny,1:nx+1])
                                            + Ax*(u[:,1:ny+1,2:nx+2]+u[:,1:ny+1,0:nx])
                                            - 2.0*(Ax+Ay)*u[:,1:ny+1,1:nx+1]
                                            + Smat[1,:,:,:]*u[:,1:ny+1,1:nx+1]
                                            + np.roll(Smat[0,:,:,:]*u[:,1:ny+1,1:nx+1],-1,axis=0)
                                            + np.roll(Smat[2,:,:,:]*u[:,1:ny+1,1:nx+1],1,axis=0)))*mask
                                         
  return u,res



def Jacrelax_axi(level,u,f, L0, Smat, f_type, mask, iters=1,pre=False):
  '''
  under-relaxed Jacobi method smoothing


  Axi symmetric routine: this is not stictly speaking a QG routine but all the
  machinery is here so...

  '''

  si = u.shape
  nx = (si[-1]-2)
  ny = (si[-2]-2)

  if f_type == 'center': # centered field
    dx = L0/nx # L0 is the last dimension
    dy = dx
  else: # nodal field
    dx = L0/(nx+1)
    dy = dx

    xx = np.linspace(0,dx*(nx+1),nx+2)
#    xx = xx[None,:]
#    xr = np.zeros((1,nx+2))
    xr = np.zeros((nx+2))
    xr[1:] = 1./xx[1:]

  Ax = 1.0/dx**2; Ay = 1.0/dy**2
  Ap = 1.0/(2.0*(Ax+Ay))

  if isinstance(mask,np.ndarray):
    mask = mask[:,1:ny+1,1:nx+1]

  #Dirichlet BC
  if f_type == 'center': # centered field
    u[:, 0,:] = -u[:, 1,:]
    u[:,-1,:] = -u[:,-2,:]
    u[:,:, 0] = -u[:,:, 1]
    u[:,:,-1] = -u[:,:,-2]
  else: # nodal field
    u[:, 0,:] = 0.
    u[:,-1,:] = 0.
    u[:,:, 0] = 0.
    u[:,:,-1] = 0.

  #if it is a pre-sweep, u is fully zero (on the finest grid depends on BC, always true on coarse grids)
  # we can save some calculation, if doing only one iteration, which is typically the case.
  if(pre and level>1):
    u[:,1:ny+1,1:nx+1] = -Ap*f[:,1:ny+1,1:nx+1]*mask
    #Dirichlet BC
    if f_type == 'center': # centered field
      u[:, 0,:] = -u[:, 1,:]
      u[:,-1,:] = -u[:,-2,:]
      u[:,:, 0] = -u[:,:, 1]
      u[:,:,-1] = -u[:,:,-2]
    else:  # nodal field
      u[:, 0,:] = 0.
      u[:,-1,:] = 0.
      u[:,:, 0] = 0.
      u[:,:,-1] = 0.

    iters = iters - 1

  for it in range(iters):
    u[:,1:ny+1,1:nx+1] = Ap*(Ay*(u[:,2:ny+2,1:nx+1] + u[:,0:ny,1:nx+1])
                         + Ax*(u[:,1:ny+1,2:nx+2] + u[:,1:ny+1,0:nx])
                         - xr[1:nx+1]/(2*dx)*(u[:,1:ny+1,2:nx+2]-u[:,1:ny+1,0:nx])
                         - xx[1:nx+1]*f[:,1:ny+1,1:nx+1])*mask
    #Dirichlet BC
    if f_type == 'center': # centered field
      u[:, 0,:] = -u[:, 1,:]
      u[:,-1,:] = -u[:,-2,:]
      u[:,:, 0] = -u[:,:, 1]
      u[:,:,-1] = -u[:,:,-2]
    else: # nodal field
      u[:, 0,:] = 0.
      u[:,-1,:] = 0.
      u[:,:, 0] = 0.
      u[:,:,-1] = 0.

#  if(not pre):
#    return u,None

  res = np.zeros_like(u)
  res[:,1:ny+1,1:nx+1] = (f[:,1:ny+1,1:nx+1]-(xr[1:nx+1]*( Ay*(u[:,2:ny+2,1:nx+1]+u[:,0:ny,1:nx+1])
                                       + Ax*(u[:,1:ny+1,2:nx+2]+u[:,1:ny+1,0:nx])
                                       - 2.0*(Ax+Ay)*u[:,1:ny+1,1:nx+1]) 
                                        - xr[1:nx+1]/(2*dx)*(u[:,1:ny+1,2:nx+2]-u[:,1:ny+1,0:nx])))*mask
  return u,res



def restrict(v, f_type):
  '''
  restrict 'v' to the coarser grid
  '''

  if not isinstance(v,np.ndarray):
    return v

  si = v.shape
  nl = si[0]

  if f_type == 'center': # centered field
    nx = (si[-1]-2)//2
    ny = (si[-2]-2)//2
    v_c = np.zeros([nl,ny+2,nx+2])

  #  #vectorized form of 
  #  for i in range(1,nx+1):
  #    for j in range(1,ny+1):
  #      v_c[i,j]=0.25*(v[2*i-1,2*j-1]+v[2*i,2*j-1]+v[2*i-1,2*j]+v[2*i,2*j])
  
    v_c[:,1:ny+1,1:nx+1]=0.25*(v[:,1:2*ny:2,1:2*nx:2]+v[:,1:2*ny:2,2:2*nx+1:2]+v[:,2:2*ny+1:2,1:2*nx:2]+v[:,2:2*ny+1:2,2:2*nx+1:2])

  else: # nodal field
    nx = (si[-1]-1)//2
    ny = (si[-2]-1)//2
    v_c = np.zeros([nl,ny+1,nx+1])
    
    v_c[:,1:-1,1:-1] = (0.25*v[:,2:-2:2,2:-2:2] +
                        0.125*(v[:,1:-3:2,2:-2:2] +
                               v[:,3:-1:2,2:-2:2] +
                               v[:,2:-2:2,1:-3:2] +
                               v[:,2:-2:2,3:-1:2]) + 
                        0.0625*(v[:,1:-3:2,1:-3:2] + 
                                v[:,1:-3:2,3:-1:2] +
                                v[:,3:-1:2,1:-3:2] +
                                v[:,3:-1:2,3:-1:2]))

  return v_c

def prolong(v, f_type):
  '''
  interpolate 'v' to the fine grid
  '''
  si = v.shape
  nl = si[0]
  if f_type == 'center': # centered field

    nx = (si[-1]-2)
    ny = (si[-2]-2)
  
    v_f=np.zeros([nl,2*nx+2,2*ny+2])
  
  #  #vectorized form of 
  #  for i in range(1,nx+1):
  #    for j in range(1,ny+1):
  #      v_f[2*i-1,2*j-1] = 0.5625*v[i,j]+0.1875*(v[i-1,j]+v[i,j-1])+0.0625*v[i-1,j-1]
  #      v_f[2*i  ,2*j-1] = 0.5625*v[i,j]+0.1875*(v[i+1,j]+v[i,j-1])+0.0625*v[i+1,j-1]
  #      v_f[2*i-1,2*j  ] = 0.5625*v[i,j]+0.1875*(v[i-1,j]+v[i,j+1])+0.0625*v[i-1,j+1]
  #      v_f[2*i  ,2*j  ] = 0.5625*v[i,j]+0.1875*(v[i+1,j]+v[i,j+1])+0.0625*v[i+1,j+1]
  
    a=0.5625; b=0.1875; c= 0.0625
  
    v_f[:,1:2*ny:2  ,1:2*nx:2  ] = a*v[:,1:ny+1,1:nx+1]+b*(v[:,0:ny  ,1:nx+1]+v[:,1:ny+1,0:nx]  )+c*v[:,0:ny  ,0:nx  ]
    v_f[:,2:2*ny+1:2,1:2*nx:2  ] = a*v[:,1:ny+1,1:nx+1]+b*(v[:,2:ny+2,1:nx+1]+v[:,1:ny+1,0:nx]  )+c*v[:,2:ny+2,0:nx  ]
    v_f[:,1:2*ny:2  ,2:2*nx+1:2] = a*v[:,1:ny+1,1:nx+1]+b*(v[:,0:ny  ,1:nx+1]+v[:,1:ny+1,2:nx+2])+c*v[:,0:ny  ,2:nx+2]
    v_f[:,2:2*ny+1:2,2:2*nx+1:2] = a*v[:,1:ny+1,1:nx+1]+b*(v[:,2:ny+2,1:nx+1]+v[:,1:ny+1,2:nx+2])+c*v[:,2:ny+2,2:nx+2]
  else: # nodal field
    nx = (si[-1]-1)
    ny = (si[-2]-1)
  
    v_f = np.zeros([nl,2*ny+1,2*nx+1])
  
    v_f[:,2:-2:2,2:-2:2] = v[:,1:-1,1:-1]
    v_f[:,1:-1:2,2:-2:2] = 0.5*(v[:,:-1,1:-1] + v[:,1:,1:-1])
    v_f[:,2:-2:2,1:-1:2] = 0.5*(v[:,1:-1,:-1] + v[:,1:-1,1:])
    v_f[:,1:-1:2,1:-1:2] = 0.25*(v[:,1:,1:] + v[:,1:,:-1] + v[:,:-1,1:] + v[:,:-1,:-1])
  
  return v_f


def V_cycle(num_levels,u,f, L0, Jacrelax, Smat, f_type, mask, level=1):
  '''
  V cycle
  '''
  if(level == num_levels):#bottom solve
    u,res = Jacrelax(level,u,f, L0, Smat, f_type, mask, iters=50,pre=True)
    return u,res

  #Step 1: Relax Au=f on this grid
  u,res = Jacrelax(level,u,f, L0, Smat, f_type, mask, iters=2,pre=True)

  #Step 2: Restrict residual to coarse grid
  #res_c=restrict(nx//2,ny//2,res)
  res_c = restrict(res, f_type)
  #res_c = qg.coarsen(res[1:-1,1:-1])
  #res_c = qg.pad_bc(res_c)

  mask_c = restrict(mask, f_type)
  #Step 3:Solve A e_c=res_c on the coarse grid. (Recursively)
  e_c = np.zeros_like(res_c)
  e_c,res_c = V_cycle(num_levels,e_c,res_c, L0, Jacrelax, Smat, f_type, mask_c, level+1)

  #Step 4: Interpolate(prolong) e_c to fine grid and add to u
  #u+=prolong(nx//2,ny//2,e_c)
  u += prolong(e_c, f_type)
  #u+= qg.pad_bc(qg.refine(e_c[1:-1,1:-1]))
  
  #Step 5: Relax Au=f on this grid
  u,res = Jacrelax(level,u,f, L0, Smat, f_type, mask, iters=1,pre=False)
  return u,res

def FMG(num_levels,f, L0, Jacrelax, f_type, mask, Smat=1, nv=1,level=1):

  if(level == num_levels):#bottom solve
    #u=np.zeros([nx+2,ny+2])  
    u = np.zeros_like(f)  
    u,res = Jacrelax(level,u,f, L0, Smat, f_type, mask, iters=50,pre=True)
    return u,res

  #Step 1: Restrict the rhs to a coarse grid
  #f_c=restrict(nx//2,ny//2,f)
  f_c = restrict(f, f_type)
  mask_c = restrict(mask, f_type)
  #f_c = qg.coarsen(f[1:-1,1:-1])
  #f_c = qg.pad_bc(f_c)

  #Step 2: Solve the coarse grid problem using FMG
  u_c,_ = FMG(num_levels,f_c, L0, Jacrelax, f_type, mask_c, Smat, nv,level+1)

  #Step 3: Interpolate u_c to the fine grid
  #u=prolong(nx//2,ny//2,u_c)
  u = prolong(u_c, f_type)
  #u = qg.pad_bc(qg.refine(u_c[1:-1,1:-1]))

  #step 4: Execute 'nv' V-cycles
  for _ in range(nv):
    u,res = V_cycle(num_levels-level,u,f, L0, Jacrelax, Smat, f_type, mask)
  return u,res

# def MGVP(nx,ny,num_levels):
#   '''
#   Multigrid Preconditioner. Returns a (scipy.sparse) LinearOperator that can
#   be passed to Krylov solvers as a preconditioner. The matrix is not 
#   explicitly needed.  All that is needed is a matrix vector product 
#   In any stationary iterative method, the preconditioner-vector product
#   can be obtained by setting the RHS to the vector and initial guess to 
#   zero and performing one iteration. (Richardson Method)  
#   '''
#   def pc_fn(v):
#     u =np.zeros([nx+2,ny+2])
#     f =np.zeros([nx+2,ny+2])
#     f[1:nx+1,1:ny+1] =v.reshape([nx,ny])
#     #perform one V cycle
#     u,res=V_cycle(nx,ny,num_levels,u,f)
#     return u[1:nx+1,1:ny+1].reshape(v.shape)
#   M=LinearOperator((nx*ny,nx*ny), matvec=pc_fn)
#   return M


# ## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
# def TDMAsolver(a, b, c, d):
#     '''
#     TDMA solver, a b c d can be NumPy array type or Python list type.
#     refer to http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
#     and to http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_(Thomas_algorithm)
#     '''
#     # a is lower diag (starts at 0)
#     # b is main diag (starts at 0)
#     # c is upper diag (starts at 0)!!!!!!!!!

#     nf = d.shape[0] # number of equations
#     ac, bc, cc, dc = map(np.array, (a, b, c, d)) # copy arrays
#     print(bc.shape, dc.shape)
#     for it in range(1, nf):
#       mc = ac[it-1,:,:]/bc[it-1,:,:]
#       bc[it,:,:] = bc[it,:,:] - mc*cc[it-1,:,:] 
#       dc[it,:,:] = dc[it,:,:] - mc*dc[it-1,:,:]


#     xc = bc
#     xc[-1,:,:] = dc[-1,:,:]/bc[-1,:,:]

#     for il in range(nf-2, -1, -1):
#         xc[il,:,:] = (dc[il,:,:]-cc[il,:,:]*xc[il+1,:,:])/bc[il,:,:]

#     return xc


def find_level(nx):
  """
  Determines the level of division of a number by repeatedly halving it
  until it is no longer divisible by 2.

  The function starts with an integer `nx` and finds how many times it 
  can be divided by 2 (i.e., how many times it can be halved) until the 
  halved value is no longer equal to half of the original value. This 
  process is repeated until no further division by 2 is possible.

  Args:
      nx (int): The integer to be repeatedly halved.

  Returns:
      int: The level (number of times the integer can be halved by 2).
  
  Example:
      >>> find_level(64)
      6
      
      >>> find_level(100)
      2
  """
  level = 0
  nx2 = int(nx/2)
  while 2*nx2 == nx:
    level += 1
    nx = nx2
    nx2 = int(nx/2)

  return level



def solve_mg(rhs, Delta, select_solver='2d', dh=1, N2=1 ,f0=1, mask=1):
  '''
  Generic function for Poisson or Laplace equation

  Parameters
  ----------

  rhs : array [(nz,) ny,nx]
  Delta: float
  select_solver: str '2d' or 'pv' or 'w'
  dh : array [nz] 
  N2 : array [nz (,ny,nx)]
  f0 : scalar or array [ny,nx]
  mask : array [ny,nx]

  Returns
  -------

  Solution psi of the selected equation:

  '2d':

       d^2        d^2      
       ---- psi + ---- psi = rhs
       dx^2       dy^2     

  'pv':

       d^2        d^2        d  ( f^2  d     ) 
       ---- psi + ---- psi + -- ( ---  -- psi) = rhs
       dx^2       dy^2       dz ( N^2  dz    ) 


  'w':

       d^2        d^2        f^2 d^2  
       ---- psi + ---- psi + --- ----  psi = rhs
       dx^2       dy^2       N^2 dz^2 

  '''


  #  L0 is the total length of the domain
  # do not change this

  nd = rhs.ndim
  
  if nd < 3:
    rhs = rhs[None,:,:]

  # nd2 = N2.ndim
  # if nd2>1:
  #   print("Does not work yet for variable N2 or f .. yet")
  #   sys.exit(1)

  nl,ny,nx = np.shape(rhs)

  if nx % 2 == 0: # centered field
    nlevels = min(find_level(nx), find_level(ny)) + 1
    #int(np.log2(min(nx,ny)) + 1)
    L0 = nx*Delta # L0 is based on the last dimension
    rhs_p = pad_bc(rhs)
    f_type = 'center'
  else: # nodal field
    nlevels = min(find_level(nx-1), find_level(ny-1)) + 1
    #int(np.log2(min(nx,ny)-1))
    L0 = (nx - 1)*Delta # L0 is based on the last dimension
    rhs_p = rhs
    f_type = 'node'


  if isinstance(mask,np.ndarray):
    mask = mask[None,:,:]


  nv = 2
  if select_solver == '2d':
    S = 1
    u,res = FMG(nlevels, rhs_p, L0, Jacrelax_2d, f_type, mask, S, nv)
  elif select_solver == 'pv':
    S = gamma_stretch(dh, N2, f0, wmode=False, squeeze=False, mat_format='diag')
    u,res = FMG(nlevels, rhs_p, L0, Jacrelax_3d, f_type, mask, S, nv)
  elif select_solver == 'w':
    S = gamma_stretch(dh, N2, f0, wmode=True, squeeze=False, mat_format='diag')
    u,res = FMG(nlevels, rhs_p, L0, Jacrelax_3d, f_type, mask, S, nv)
  elif select_solver == 'axi':
    S = 1
    u,res = FMG(nlevels, rhs_p, L0, Jacrelax_axi, f_type, mask, S, nv)

  if f_type == 'center': # centered field
    u = u[:,1:-1,1:-1]


  if nd < 3:
    return u[0,:,:]
  else:
    return u



