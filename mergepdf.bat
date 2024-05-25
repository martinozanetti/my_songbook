@echo off
setlocal

REM Check if IrfanView is installed
if not exist "C:\Program Files\IrfanView\i_view64.exe" (
    echo IrfanView is not installed. Please install IrfanView and try again.
    exit /b 1
)

REM Check if the correct number of arguments is provided
if "%~3"=="" (
    echo Usage: merge_pdfs.bat file1.pdf file2.pdf output.pdf
    exit /b 1
)

REM Set variables for input and output files
set "file1=%~1"
set "file2=%~2"
set "output=%~3"

REM Merge the PDF files
"C:\Program Files\IrfanView\i_view64.exe" "%file1%" /append="%file2%" /convert="%output%"

REM Check if the merge was successful
if %errorlevel% neq 0 (
    echo Failed to merge PDF files.
    exit /b 1
)

echo PDF files merged successfully into %output%.

endlocal
exit /b 0
