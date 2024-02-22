echo off
echo Make sure that Miniconda3-latest-Windows-x86_64 is installed!

set MINICONDA_PATH=D:\Miniconda3
set /p MINICONDA_PATH=Please insert Miniconda directory path (default - %MINICONDA_PATH%):
echo Miniconda Path: %MINICONDA_PATH%


call %MINICONDA_PATH%\condabin\conda config --set ssl_verify no
call %MINICONDA_PATH%\condabin\conda env update -f environment.yml
call %MINICONDA_PATH%\condabin\conda activate python310

set PYTHON3PATH=C:\python310
mklink /J %PYTHON3PATH% %MINICONDA_PATH%\envs\python310
pause