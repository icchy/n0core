import os
import ast


def extractpb(fname):
    tree = ast.parse(open(fname).read())
    for t in tree.body:
        if not isinstance(t, ast.Assign):
            continue

        if isinstance(t.value, ast.Call) \
                and t.value.func.value.id == '_reflection' \
                and t.value.func.attr == 'GeneratedProtocolMessageType':
            yield t.targets[0].id


for curdir, dirs, files in os.walk('.'):
    for fname in files:
        if not fname.endswith('.py'):
            continue
        for name in extractpb(os.path.join(curdir, fname)):
            print('from {} import {}  # noqa'.format(os.path.join(curdir, fname[:-3])[1:].replace('/', '.'), name))
