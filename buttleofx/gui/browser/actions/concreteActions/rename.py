import os
from buttleofx.gui.browser.actions.actionInterface import ActionInterface


class Rename(ActionInterface):

    def __init__(self, browserItem, newName):
        ActionInterface.__init__(self, browserItem)
        self._newName = newName
        self._oldName = browserItem.getName()

    def execute(self):
        browserItem = self._browserItem

        # Rename File
        if browserItem.isFile():
            # TODO: Check permission in try catch
            path = browserItem.getParentPath()
            oldFilePath = os.path.join(path, browserItem.getName())
            newFileName = self._newName
            newFilePath = os.path.join(path, newFileName)

            # Add extension if filename miss it
            if not os.path.splitext(newFilePath)[1]:
                oldFileExtension = os.path.splitext(oldFilePath)[1]
                newFileName += oldFileExtension

            self.__rename(browserItem.getParentPath(),
                          browserItem.getName(),
                          newFileName)
            # os.rename(oldFilePath, newFilePath)
            # browserItem.updatePath(newFilePath)

        # Rename Folder
        if browserItem.isFolder():
            # TODO: Check permission in try catch
            self.__rename(browserItem.getParentPath(),
                          browserItem.getName(),
                          self._newName)
            # path = browserItem.getParentPath()
            # oldPath = os.path.join(path, browserItem.getName())
            # newPath = os.path.join(path, self._newName)
            # os.rename(oldPath, newPath)
            # browserItem.updatePath(newPath)

        # TODO: Rename sequence
        if browserItem.isSequence():
            seqParsed = browserItem.getSequence().getSequenceParsed()
            frames = seqParsed.getFramesIterable()

            for f in frames:
                newFrameName = seqParsed.getFilenameAt(f)\
                                        .replace(seqParsed.getPrefix(),
                                                 self._newName)
                self.__rename(browserItem.getParentPath(),
                              seqParsed.getFilenameAt(f),
                              newFrameName)

    def revert(self):
        browserItem = self._browserItem

        if browserItem.isFile():
            self.__rename(browserItem.getParentPath(),
                          browserItem.getName(),
                          self._oldName)

        if browserItem.isFolder():
            self.__rename(browserItem.getParentPath(),
                          browserItem.getName(),
                          self._oldName)

        if browserItem.isSequence():
            seqParsed = browserItem.getSequence().getSequenceParsed()
            frames = seqParsed.getFramesIterable()

            for f in frames:
                newFrameName = seqParsed.getFilenameAt(f) \
                               .replace(seqParsed.getPrefix(),
                                        self._newName)
                self.__rename(browserItem.getParentPath(),
                              newFrameName,
                              seqParsed.getFilenameAt(f))
    # Private Methods
    def __rename(self, basePath, oldName, newName):
        oldPath = os.path.join(basePath, oldName)
        newPath = os.path.join(basePath, newName)
        os.rename(oldPath, newPath)
        self._browserItem.updatePath(newPath)
