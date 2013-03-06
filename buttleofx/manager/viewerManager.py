# quickmamba
from quickmamba.patterns import Singleton
# Tuttle
from pyTuttle import tuttle
# data
from buttleofx.data import ButtleDataSingleton


class ViewerManager(Singleton):
    """
        This class manages actions about the viewer.
    """

    def __init__(self):
	    self._tuttleImageCache = None
	    self._computedImage = None

    def computeNode(self, frame):
        """
            Compute the node at the frame indicated
        """
        print "------- COMPUTE NODE -------"

        buttleData = ButtleDataSingleton().get()
        #Get the name of the currentNode of the viewer
        node = buttleData.getCurrentViewerNodeName()

        #Get the output where we save the result
        self._tuttleImageCache = tuttle.MemoryCache()
        #should replace 25 by the fps of the video (a sort of getFPS(node))
        #should expose the duration of the video to the QML too
        buttleData.getGraph().getGraphTuttle().compute(self._tuttleImageCache, node, tuttle.ComputeOptions(int(frame)))
        self._computedImage = self._tuttleImageCache.get(0)

        #Add the computedImage to the map
        buttleData._mapNodeNameToComputedImage.update({node: self._computedImage})

        return self._computedImage

    def retrieveImage(self, frame, frameChanged):
        """
            Compute the node at the frame indicated if the frame has changed (if the time has changed)
        """
        buttleData = ButtleDataSingleton().get()
        #Get the name of the currentNode of the viewer
        node = buttleData.getCurrentViewerNodeName()
        #Get the map
        mapNodeToImage = buttleData._mapNodeNameToComputedImage

        try:
            buttleData.setNodeError("")
            #If the image is already calculated
            for element in mapNodeToImage:
                if node == element and frameChanged is False:
                    print "**************************Image already calculated**********************"
                    return buttleData._mapNodeNameToComputedImage[node]
                # If it is not
            print "************************Calcul of image***************************"
            return self.computeNode(frame)
        except Exception as e:
            print "Can't display node : " + node
            buttleData.setNodeError(str(e))
            raise