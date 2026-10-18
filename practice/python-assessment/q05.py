import sys

class Model:
    framework = "CAME-ML"   # class variable

    def __init__(self, name):
        self.name = name


for line in sys.stdin:
    line = line.strip()

    # ignore blanks and comments
    if not line or line.startswith("#"):
        continue

    parts = line.split(maxsplit=1)

    # FRAMEWORK update line
    if parts[0] == "FRAMEWORK":
        Model.framework = parts[1] if len(parts) > 1 else ""
    else:
        # model registration
        model_name = parts[0]
        m = Model(model_name)
        print(f"{m.name}|{Model.framework}")