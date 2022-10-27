# -*- mode: python ; coding: utf-8 -*-
import os


base_venv = os.environ['CONDA_PREFIX']

block_cipher = None


a = Analysis(['st_run.py'],
             pathex=[],
             binaries=[],
             datas=[
                 (
                     os.path.join(base_venv, "Lib/site-packages/altair/vegalite/v4/schema/vega-lite-schema.json"),
                     "./altair/vegalite/v4/schema/"
                 ),
                 (
                      os.path.join(base_venv, "Lib/site-packages/streamlit/static"),
                     "./streamlit/static"
                 )
            ],
             hiddenimports=[],
             hookspath=['c:\\work\\pat\\hooks'],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='st_run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
