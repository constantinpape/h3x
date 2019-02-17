import os
from .replace_word import replace_stl


def refactor_sizet(root_folder, extensions=['.h', '.c',
                                            '.hxx', '.cxx',
                                            '.hpp', '.cpp']):
    for root, dirs, files in os.walk(root_folder):
        for name in files:
            ext = os.path.splitext(name)[1]
            if ext not in extensions:
                continue
            replace_stl(os.path.join(root, name), 'size_t')
