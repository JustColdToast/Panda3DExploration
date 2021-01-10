from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor  # An actor represents an animated model
from direct.interval.IntervalGlobal import Sequence  # Allows the start of a background task on an interval
from panda3d.core import Point3


class MyApp(ShowBase):  # Creates class TestApp, inherits from showbase class of Panda3D

    def __init__(self):  # Initializes the scene
        ShowBase.__init__(self)
        self.disableMouse()  # Prevents mouse from interfering with camera controls
        # Load a 3D model to the variable "scene"
        # .loadModel is used for static models, which do not need to be animated
        self.scene = self.loader.loadModel("models/environment")
        # Add the model to the parent window, allowing it to be rendered
        self.scene.reparentTo(self.render)
        # Scale the model to fit the screen
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # A manager is needed to time and execute "tasks"
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load an actor for a panda model
        self.panda = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.panda.setScale(0.005, 0.005, 0.005)
        self.panda.reparentTo(self.render)  # Re-parent model to allow render
        # Earlier, when panda model was loaded, a sub animation was created in a dictionary
        # This model was called: "walk," with an associated animation loaded
        # Below line references the declared walk animation for the model associated with variable panda
        # It then loops this animation
        self.panda.loop("walk")

    def spinCameraTask(self, task):  # This function allows enhanced movement of the view camera
        # It represents a "task," which is a function that is called on every frame
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi/180)
        self.camera.setPos(20*sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont  # Hand off execution to the task manager

app = MyApp()
app.run()