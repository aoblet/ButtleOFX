from PySide import QtCore


class Double3DWrapper(QtCore.QObject):
    def __init__(self, param):
        QtCore.QObject.__init__(self)
        self._param = param
        self._param.changed.connect(self.emitChanged)

    #################### getters ####################

    def getParamType(self):
        return self._param.paramType

    def getText(self):
        return self._param.text

    def getDefaultValue1(self):
        return self._param.defaultValue1

    def getDefaultValue2(self):
        return self._param.defaultValue2

    def getDefaultValue3(self):
        return self._param.defaultValue3

    def getValue1(self):
        return self._param.value1

    def getValue2(self):
        return self._param.value2

    def getValue3(self):
        return self._param.value3

    def getMaximum(self):
        return self._param.maximum

    def getMinimum(self):
        return self._param.minimum

    #################### setters ####################

    def setParamType(self, paramType):
        self._param.paramType = paramType

    def setText(self, text):
        self._param.text = text

    def setDefaultValue1(self, defaultValue1):
        self._param.defaultValue1 = defaultValue1

    def setDefaultValue2(self, defaultValue2):
        self._param.defaultValue2 = defaultValue2

    def setDefaultValue3(self, defaultValue3):
        self._param.defaultValue3 = defaultValue3

    def setValue1(self, value1):
        self._param.value1 = value1

    def setValue2(self, value2):
        self._param.value2 = value2

    def setValue3(self, value3):
        self._param.value3 = value3

    def setMaximum(self, maximum):
        self._param.maximum = maximum

    def setMinimum(self, minimum):
        self._param.minimum = minimum

    @QtCore.Signal
    def changed(self):
        pass

    def emitChanged(self):
        self.changed.emit()

    paramType = QtCore.Property(unicode, getParamType, setParamType, notify=changed)
    text = QtCore.Property(unicode, getText, setText, notify=changed)
    value1 = QtCore.Property(float, getValue1, setValue1, notify=changed)
    value2 = QtCore.Property(float, getValue2, setValue2, notify=changed)
    value3 = QtCore.Property(float, getValue3, setValue2, notify=changed)
    maximum = QtCore.Property(float, getMaximum, setMaximum, notify=changed)
    minimum = QtCore.Property(float, getMinimum, setMinimum, notify=changed)
