try:
    value = float("abc")
except Exception:
    print("Exception")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")