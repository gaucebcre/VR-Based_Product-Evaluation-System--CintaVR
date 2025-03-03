# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all submodules needed for matplotlib, pandas, and seaborn
hiddenimports = collect_submodules('matplotlib') + collect_submodules('pandas') + collect_submodules('seaborn')

# Collect additional data files needed by these libraries (e.g., configuration files from matplotlib)
datas = collect_data_files('matplotlib') + collect_data_files('pandas') + collect_data_files('seaborn')

# Analysis configuration
a = Analysis(
    ['interface.py'],  # Your main script
    pathex=[],  # Additional directories if needed
    binaries=[],  # Any additional binary files you might need
    datas=[('DrawPosition.py', '.'), 
           ('PositionHeatmap.py', '.'), 
           ('EyeTracking.py', '.')],  # Ensuring your scripts are included in the executable
    hiddenimports=hiddenimports,  # Additional dependencies that might not be automatically detected
    hookspath=[],  # If you have custom hooks, you can add them here
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],  # Libraries you don't need to include
    noarchive=False,  # This makes everything be packed in the .exe instead of in a compressed file
    optimize=0,
)

# Create the PYZ file
pyz = PYZ(a.pure)

# Executable configuration
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='interface',  # Name of the executable file
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # This optimizes the size of the executable (if compatible)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Disables the console window (ideal for GUIs)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


