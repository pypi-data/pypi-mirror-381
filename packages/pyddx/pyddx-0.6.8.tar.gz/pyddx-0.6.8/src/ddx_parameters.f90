!> @copyright (c) 2020-2021 RWTH Aachen. All rights reserved.
!!
!! ddX software
!!
!! @file src/ddx_parameters.f90
!! The type ddx_params_type is defined here along with its routines meant to
!! init, deinit and read it from a file in certain fromats. All the new code to
!! read user input from different file formats shall be added here.
!!
!! @version 1.0.0
!! @author Aleksandr Mikhalev
!! @date 2021-06-15

!> Module to treat properly user input parameters
module ddx_parameters
! Include compile-time definitions
use ddx_definitions
use ddx_errors
! Enable OpenMP 
use omp_lib
implicit none


!> Type to check and store user input parameters
type ddx_params_type
    !> Model to use 1 for COSMO, 2 for PCM, 3 for LPB.
    integer :: model
    !> Whether computing analytical forces will be required (1) or not (0).
    integer :: force
    !> Relative dielectric permittivity.
    real(dp) :: eps
    !> Debye-H\"{u}ckel parameter. Referenced only in LPB model (model=3)
    real(dp) :: kappa
    !> Regularization parameter.
    real(dp) :: eta
    !> Shift of the regularization. -1 for interior, 0 for centered and
    !! 1 for outer regularization.
    real(dp) :: se
    !> Maximal degree of modeling spherical harmonics.
    integer :: lmax
    !> Number of Lebedev grid points on each sphere.
    integer :: ngrid
    !> Maximum number of iterations for the iterative solver.
    integer :: maxiter
    !> Number of extrapolation points for Jacobi/DIIS solver. Referenced only
    !! if Jacobi solver is used.
    integer :: jacobi_ndiis
    !> Enable (1) or disable (0) use of FMM techniques.
    integer :: fmm
    !> Maximal degree of spherical harmonics for a multipole expansion.
    !! If this value is -1 then no far-field FMM interactions are performed.
    integer :: pm
    !> Maximal degree of spherical harmonics for a local expansion.
    !! If this value is -1 then no far-field FMM interactions are performed.
    integer :: pl
    !> Number of OpenMP threads to be used. Currently, only nproc=1 is
    !! supported as the ddX is sequential right now.
    integer :: nproc
    !> Number of atoms in the molecule.
    integer :: nsph
    !> Centers of atoms of a dimension (3, nsph).
    real(dp), allocatable :: csph(:, :)
    !> Array of radii of atoms of a dimension (nsph).
    real(dp), allocatable :: rsph(:)
    !> Dielectric permittivity of the cavity (used by ddLPB), hardcoded to one
    real(dp) :: epsp = 1.0_dp
    !> integer matvecmem. Build hsp matrix to speed up matrix-vec product
    integer :: matvecmem
    !> variable to enable debug printins:
    !> fname: name of the output file
    character(len=255) :: output_filename
    !> len_fname: actual length of the output file
    integer :: len_output_filename
    !> verbose: true if printing is enabled
    logical :: verbose
    !> output unit
    integer :: iunit
end type ddx_params_type

contains

!> Initialize and check input parameters
!!
!! @param[in] model: Choose model: 1 for COSMO, 2 for PCM and 3 for LPB.
!! @param[in] force: 1 if forces will probably be required and 0 otherwise.
!! @param[in] eps: Relative dielectric permittivity. eps > 1.
!! @param[in] kappa: Debye-H\"{u}ckel parameter. kappa > 0. Referenced
!!      only if the model is LPB.
!! @param[in] eta: Regularization parameter. 0 < eta <= 1.
!! @param[in] se: Shift of the regularization. -1 for interior, 0 for
!!      centered and 1 for outer regularization.
!! @param[in] lmax: Maximal degree of modeling spherical harmonics.
!!      `lmax` >= 0.
!! @param[in] ngrid: Number of Lebedev grid points `ngrid` >= 0.
!! @param[in] matvecmem: handling of sparse matrices. 1 for precomputing them 
!!      and keeping them in memory, 0 for direct matrix-vector products.
!! @param[in] maxiter: Maximum number of iterations for an iterative solver.
!!      maxiter > 0.
!! @param[in] jacobi_ndiis: Number of extrapolation points for Jacobi/DIIS solver.
!!      ndiis >= 1.
!! @param[in] fmm: 1 to use FMM acceleration and 0 otherwise.
!! @param[in] pm: Maximal degree of multipole spherical harmonics. Ignored in
!!      the case `fmm=0`. Value -1 means no far-field FMM interactions are
!!      computed. `pm` >= -1.
!! @param[in] pl: Maximal degree of local spherical harmonics. Ignored in
!!      the case `fmm=0`. Value -1 means no far-field FMM interactions are
!!      computed. `pl` >= -1.
!! @param[in] nproc: Number of OpenMP threads to be used where applicable.
!!      nproc >= 0. If input nproc=0 then a default number of threads,
!!      controlled by the environment variable `OMP_NUM_THREADS` during
!!      runtime, will be used. If OpenMP support in ddX is
!!      disabled, only possible input values are 0 or 1 and both inputs lead
!!      to the same output nproc=1 since the library is not parallel.
!! @param[in] nsph: Number of atoms. nsph > 0.
!! @param[in] csph: Coordinates of atoms. Dimension is `(3, nsph)`.
!! @param[in] rsph: Van-der-Waals radii of atoms. Dimension is `(nsph)`.
!! @param[in] output_filename: file name of log file.
!! @param[out] params: Object containing all inputs.
!! @param[inout] ddx_error: ddX error
subroutine params_init(model, force, eps, kappa, eta, se, lmax, ngrid, &
        & matvecmem, maxiter, jacobi_ndiis, fmm, pm, pl, nproc, nsph, &
        & csph, rsph, output_filename, params, ddx_error)
    !! Inputs
    ! Model to use 1 for COSMO, 2 for PCM, 3 for LPB.
    integer, intent(in) :: model
    ! Whether computing analytical forces will be required (1) or not (0).
    integer, intent(in) :: force
    ! Relative dielectric permittivity.
    real(dp), intent(in) :: eps
    ! Debye-H\"{u}ckel parameter. Referenced only in LPB model (model=3)
    real(dp), intent(in) :: kappa
    ! Regularization parameter.
    real(dp), intent(in) :: eta
    ! Shift of the regularization. -1 for interior, 0 for centered and
    !      1 for outer regularization.
    real(dp), intent(in) :: se
    ! Maximal degree of modeling spherical harmonics.
    integer, intent(in) :: lmax
    ! Number of Lebedev grid points on each sphere.
    integer, intent(in) :: ngrid
    ! handling of sparse matrix. 1 for precomputing them and keeping them in
    ! memory, 0 for assembling the mvps on-the-fly.
    integer, intent(in) :: matvecmem
    ! Maximum number of iterations for the iterative solver.
    integer, intent(in) :: maxiter
    ! Number of extrapolation points for Jacobi/DIIS solver. Referenced only
    !      if Jacobi solver is used.
    integer, intent(in) :: jacobi_ndiis
    ! Enable (1) or disable (0) use of FMM techniques.
    integer, intent(in) :: fmm
    ! Maximal degree of spherical harmonics for a multipole expansion.
    !
    ! If this value is -1 then no far-field FMM interactions are performed.
    integer, intent(in) :: pm
    ! Maximal degree of spherical harmonics for a local expansion.
    !
    ! If this value is -1 then no far-field FMM interactions are performed.
    integer, intent(in) :: pl
    ! Number of OpenMP threads to be used. 
    integer, intent(in) :: nproc
    ! Number of atoms in the molecule.
    integer, intent(in) :: nsph
    ! Centers of atoms of a dimension (3, nsph).
    real(dp), intent(in) :: csph(3, nsph)
    ! Array of radii of atoms of a dimension (nsph).
    real(dp), intent(in) :: rsph(nsph)
    ! log file name
    character(len=255) :: output_filename
    !! Outputs
    type(ddx_params_type), intent(out) :: params
    type(ddx_error_type), intent(inout) :: ddx_error
    !! Local variables
    integer :: igrid, i, info
    !! The code
    if (ddx_error % flag .ne. 0) then
        call update_error(ddx_error, "params_init received input in ddx_error " // &
            & " state, exiting")
    end if
    ! parse the log file name
    if (len(trim(output_filename)) .ne. 0) then
        params % output_filename = output_filename
        params % verbose = .true.
        params % len_output_filename = len(trim(output_filename))
    else
        params % output_filename = ''
        params % verbose = .false.
        params % len_output_filename = 0
    end if
    ! Model, 1=COSMO, 2=PCM, 3=LPB
    if ((model .lt. 1) .or. (model .gt. 3)) then
        call update_error(ddx_error, "params_init: invalid value of `model`")
    end if
    params % model = model
    ! Check if forces are needed
    if ((force .lt. 0) .or. (force .gt. 1)) then
        call update_error(ddx_error, "params_init: invalid value of `force`")
    end if
    params % force = force
    ! Relative dielectric permittivity
    if (eps .le. one) then
        call update_error(ddx_error, "params_init: invalid value of `eps`")
    end if
    params % eps = eps
    ! Debye-H\"{u}ckel parameter (only used in ddLPB)
    if ((model .eq. 3) .and. (kappa .le. zero)) then
        call update_error(ddx_error, "params_init: invalid value of `kappa`")
    end if
    params % kappa = kappa
    ! Regularization parameter
    if ((eta .lt. zero) .or. (eta .gt. one)) then
        call update_error(ddx_error, "params_init: invalid value of `eta`")
    end if
    params % eta = eta
    ! Shift of a regularization
    if ((se .lt. -one) .or. (se .gt. one)) then
        call update_error(ddx_error, "params_init: invalid value of `se`")
    end if
    params % se = se
    ! Degree of modeling spherical harmonics
    if (lmax .lt. 0) then
        call update_error(ddx_error, "params_init: invalid value of `lmax`")
    end if
    params % lmax = lmax
    ! Check number of Lebedev grid points
    igrid = 0
    do i = 1, nllg
        if (ng0(i) .eq. ngrid) then
            igrid = i
            exit
        end if
    end do
    if (igrid .eq. 0) then
        call update_error(ddx_error, "params_init: Unsupported value of `ngrid`")
    end if
    params % ngrid = ngrid
    ! Maximum number of iterations
    if (maxiter .le. 0) then
        call update_error(ddx_error, "params_init: invalid value of `maxiter`")
    end if
    params % maxiter = maxiter
    ! Number of Jacobi DIIS extrapolation points (ndiis=25 works)
    if (jacobi_ndiis .lt. 0) then
        call update_error(ddx_error, "params_init: invalid value of `jacobi_ndiis`")
    end if
    params % jacobi_ndiis = jacobi_ndiis
    ! Check if FMM-acceleration is needed
    if ((fmm .lt. 0) .or. (fmm .gt. 1)) then
        call update_error(ddx_error, "params_init: invalid value of `fmm`")
    end if
    params % fmm = fmm
    ! Set FMM parameters if FMM is needed
    if (fmm .eq. 1) then
        ! Maximal degree of multipole spherical harmonics. Value -1 means no 
        ! far-field interactions are to be computed, only near-field
        ! interactions are taken into account.
        if (pm .lt. -1) then
            call update_error(ddx_error, "params_init: invalid value of `pm`")
        end if
        ! Maximal degree of local spherical harmonics. Value -1 means no 
        ! far-field interactions are to be computed, only near-field
        ! interactions are taken into account.
        if (pl .lt. -1) then
            call update_error(ddx_error, "params_init: invalid value of `pl`")
        end if
        ! If far-field interactions are to be ignored
        if ((pl .eq. -1) .or. (pm .eq. -1)) then
            params % pm = -1
            params % pl = -1
        ! If far-field interactions are to be taken into account
        else
            params % pm = pm
            params % pl = pl
        end if
    else
        ! These values are ignored if fmm flag is 0
        params % pm = -2
        params % pl = -2
    end if
    ! Number of OpenMP threads to be used
    ! available.
    if (nproc .lt. 0) then
        call update_error(ddx_error, "params_init: invalid value of `nproc`")
        params % nproc = 1
    else if (nproc .eq. 0) then
        params % nproc = 1
    else
        params % nproc = nproc
    end if
    call omp_set_num_threads(params % nproc)
    ! Number of atoms
    if (nsph .le. 0) then
        call update_error(ddx_error, "params_init: invalid value of `nsph`")
    end if
    params % nsph = nsph
    allocate(params % csph(3, nsph), params % rsph(nsph), stat=info)
    if (info .ne. 0) then
        call update_error(ddx_error, "params_init: `csph` and `rsph` " // &
            & "allocations failed")
        return
    end if
    params % csph = csph
    params % rsph = rsph
    if (matvecmem.eq.0 .or. matvecmem.eq.1) then
        params % matvecmem = matvecmem
    else
        call update_error(ddx_error, "params_init: invalid value of `matvecmem`")
    end if

    if (ddx_error % flag .ne. 0) return

    ! init log
    call init_printing(params, ddx_error)
    if (ddx_error % flag .ne. 0) then
        call update_error(ddx_error, "init_printing returned an error, exiting")
        return
    end if
end subroutine params_init

!> Adjust a guess for the number of Lebedev grid points.
!!
!! @param[inout] ngrid: Approximate number of Lebedev grid points on input and
!!      actual number of grid points on exit. `ngrid` >= 0
subroutine closest_supported_lebedev_grid(ngrid)
    integer, intent(inout) :: ngrid
    integer :: igrid, i, inear, jnear
    ! Get nearest number of Lebedev grid points
    igrid = 0
    inear = 100000
    do i = 1, nllg
        jnear = abs(ng0(i) - ngrid)
        if (jnear .lt. inear) then
            inear = jnear
            igrid = i
        end if
    end do
    ngrid = ng0(igrid)
end subroutine

!> Deallocate the parameter object
!!
!! @param[out] params: User specified parameters
!! @param[inout] ddx_error: ddX error
!!
subroutine params_free(params, ddx_error)
    implicit none
    type(ddx_params_type), intent(inout) :: params
    type(ddx_error_type), intent(inout) :: ddx_error
    integer :: istat

    call finalize_printing(params)

    if (allocated(params % csph)) then
        deallocate(params % csph, stat=istat)
        if (istat .ne. 0) then
            call update_error(ddx_error, "params_free: `csph` deallocation failed")
        end if
    end if
    if (allocated(params % rsph)) then
        deallocate(params % rsph, stat=istat)
        if (istat .ne. 0) then
            call update_error(ddx_error, "params_free: `rsph` deallocation failed")
        end if
    end if
end subroutine params_free

!> Open the log file.
subroutine init_printing(params, ddx_error)
    implicit none
    type(ddx_params_type), intent(inout) :: params
    type(ddx_error_type), intent(inout) :: ddx_error
    logical :: exists
    if (.not.params % verbose) return
    inquire(file=params % output_filename(1:params % len_output_filename), &
        & exist=exists)
    if (exists) then
        call update_error(ddx_error, 'Log file already present')
        return
    else
        params % iunit = 100
        open(params % iunit, &
            & file=params % output_filename(1: params % len_output_filename), &
            & form='formatted')
    end if
end subroutine init_printing

!> Close the log file.
subroutine finalize_printing(params)
    implicit none
    type(ddx_params_type), intent(inout) :: params
    if (.not.params % verbose) return
    close(params % iunit)
    params % verbose = .false.
    params % output_filename = ''
    params % len_output_filename = 0
    params % iunit = 0
end subroutine finalize_printing

end module ddx_parameters
