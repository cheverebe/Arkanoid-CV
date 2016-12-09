import subprocess


class ScreenUtils(object):
    @staticmethod
    def get_screen_resolution():
        output = \
            subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0]
        return list(reversed([int(v) for v in output.split()[0].split(b'x')]))