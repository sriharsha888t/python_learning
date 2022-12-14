import warnings
warnings.simplefilter("error",UserWarning)
print("before warning")
warnings.warn("this is warning message")
print("after warning")
