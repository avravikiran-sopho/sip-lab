import sys
import os.path
p=os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(p)

import main as m

sys.path.remove(p)
m.SiplabApp().run()
print("ok")
