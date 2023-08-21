import pathlib

# TODO: should be part of lib method checking for starter package... ("core" by default)

from src.core.__main__ import main #@UnresolvedImport 

def test_core_package_exists():
    working_dir_path = pathlib.Path('src/core')
    assert working_dir_path.is_dir()
    file_path = pathlib.Path('src/core/__main__.py')
    assert file_path.is_file()
    
def test_import_possible():
    # import src.core #@UnresolvedImport
    
    # from src.core.__main__ import main #@UnresolvedImport
    
         
    # print(f'dir(src.core) {dir(src.core)}')
    # print(f'src.core.__name__ {src.core.__name__}')
    # print(f'src.core.__file__ {src.core.__file__}')
    # print(f'src.core.__package__ {src.core.__package__}')
    # print(f'dir(src.core.__package__) {dir(src.core.__package__)}')
    
    main()
    
    assert False
    
def test_import_possible2():
    # import src.core #@UnresolvedImport
    
    # from src.core.__main__ import main #@UnresolvedImport
    
         
    # print(f'dir(src.core) {dir(src.core)}')
    # print(f'src.core.__name__ {src.core.__name__}')
    # print(f'src.core.__file__ {src.core.__file__}')
    # print(f'src.core.__package__ {src.core.__package__}')
    # print(f'dir(src.core.__package__) {dir(src.core.__package__)}')
    
    main()
    
    assert False
    
def test_import_possible3():
    # import src.core #@UnresolvedImport
    
    # from src.core.__main__ import main #@UnresolvedImport
    
         
    # print(f'dir(src.core) {dir(src.core)}')
    # print(f'src.core.__name__ {src.core.__name__}')
    # print(f'src.core.__file__ {src.core.__file__}')
    # print(f'src.core.__package__ {src.core.__package__}')
    # print(f'dir(src.core.__package__) {dir(src.core.__package__)}')
    
    main()
    
    assert False
    
