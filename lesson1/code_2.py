from my_module import another_lib
import my_module
from my_module.another_lib import hello
another_lib.hello()
my_module.another_lib.hello()
hello()
