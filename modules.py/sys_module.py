import sys 

print(sys.version)

print(sys.abiflags)

print(sys.argv[0])
print(sys.argv)
print(sys.argv[:])
print(sys.base_exec_prefix)
print(sys.base_prefix)
print(sys.byteorder)

import sys


if sys.byteorder == "little":
    print("little-endian platform.")
else:
    print("big-endian platform.")

#print(sys.builtin_module_names)
#print(sys.modules.keys())

print(sys.copyright)


print(sys.platform)

print(sys._current_frames())

print(sys.exec_prefix)

print(sys.executable)

print(sys.__stdin__)

print(sys.float_info)

print(sys.float_repr_style)

print(sys.getallocatedblocks())

print(sys.getcheckinterval())

print(sys.getdefaultencoding())

print(sys.platform)