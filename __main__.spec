# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['D:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\walking-pad-obs-widget\\walking-pad-obs-widget\\Lib\\site-packages', 'D:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\walking-pad-obs-widget'],
             binaries=[],
             datas=[],
             hiddenimports=['websockets.legacy.server'],
             hookspath=[],
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
          name='__main__',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='D:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\icon.ico')
