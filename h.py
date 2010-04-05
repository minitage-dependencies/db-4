import sys
import shutil
import os
def h(o, b):
    

    if sys.platform.startswith('cygwin'):
        import pdb;pdb.set_trace()
        dest = o['compile-directory']
        ddest = "%s/%s/dist" % (
            b['buildout']['directory']+"/__minitage__part__tmp",
            os.listdir(b['buildout']['directory']+"/__minitage__part__tmp")[0]
        )
        # for f in ddest+'/aclocal/libtool.m4',ddest+'/config.sub',ddest+'/config.guess', ddest+'/ltmain.sh':
            # os.remove(f)
        # lt_dir='/usr/share/libtool/config'
        # shutil.copy2('/usr/share/aclocal/libtool.m4', ddest+'/aclocal/libtool.m4')
        # shutil.copy2(lt_dir+'/config.sub', ddest+'/config.sub')
        # shutil.copy2(lt_dir+'/config.guess', ddest+'/config.guess')
        # shutil.copy2(lt_dir+'/ltmain.sh', ddest+'/ltmain.sh')
        # cwd = os.getcwd()
        # os.chdir(ddest)
        # os.system('autoreconf')
        # os.chdir(cwd)
        
