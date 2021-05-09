# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/Bibliotheken/Desktop/Skripte/ginos-walking-pad/walking-pad-obs-widget/__main__.py'],
             pathex=['D:/Bibliotheken/Desktop/Skripte/ginos-walking-pad/walking-pad-obs-widget/ginos-walking-pad/Lib/site-packages', 'D:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\walking-pad-obs-widget'],
             binaries=[],
             datas=[],
             hiddenimports=[" d:; cd 'd:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\walking-pad-obs-widget'; & 'd:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\walking-pad-obs-widget\\ginos-walking-pad\\Scripts\\python.exe' 'c:\\Users\\timm_\\.vscode\\extensions\\ms-python.python-2021.4.765268190\\pythonFiles\\lib\\python\\debugpy\\launcher' '50439' '--' 'd:\\Bibliotheken\\Desktop\\Skripte\\ginos-walking-pad\\walking-pad-obs-widget\\__main__.py' miio"],
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
