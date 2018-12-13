import vtk

class MouseInteractorHighLightActor(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self, parent=None):
        self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)

        self.LastPickedActor = None
        self.LastPickedProperty = vtk.vtkProperty()

    def leftButtonPressEvent(self, obj, event):
        clickPos = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkPropPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.GetDefaultRenderer())
        self.NewPickedActor = picker.GetActor()
        if self.NewPickedActor:
            # If we picked something before, reset its property
            if self.LastPickedActor:
                self.LastPickedActor.GetProperty().DeepCopy(self.LastPickedProperty)
            self.LastPickedProperty.DeepCopy(self.NewPickedActor.GetProperty())
            self.NewPickedActor.GetProperty().SetColor(0.0, 1.0, 1.0)
            self.NewPickedActor.GetProperty().SetDiffuse(1.0)
            self.NewPickedActor.GetProperty().SetSpecular(0.0)
            self.LastPickedActor = self.NewPickedActor
        self.OnLeftButtonDown()
        return

renderer = vtk.vtkRenderer()
renderer.SetBackground(1.0,0.0,1.0)

renwin = vtk.vtkRenderWindow()
renwin.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renwin)

style = MouseInteractorHighLightActor()
style.SetDefaultRenderer(renderer)
interactor.SetInteractorStyle(style)

sphereSource1 = vtk.vtkSphereSource()
sphereSource1.SetCenter(-12.0, 5.0, 5.0)
sphereSource1.SetRadius(7.0)

sphereSource2 = vtk.vtkSphereSource()
sphereSource2.SetCenter(-6.0, 3.0, 0.0)
sphereSource2.SetRadius(5.0)

sphereSource3 = vtk.vtkSphereSource()
sphereSource3.SetCenter(0.0, -5.0,5.0)
sphereSource3.SetRadius(4.0)

sphereSource4 = vtk.vtkSphereSource()
sphereSource4.SetCenter(6.0, 9.0, 0.0)
sphereSource4.SetRadius(4.0)

sphereSource5 = vtk.vtkSphereSource()
sphereSource5.SetCenter(12.0, 0.0, 0.0)
sphereSource5.SetRadius(6.0)

sphereSource6 = vtk.vtkSphereSource()
sphereSource6.SetCenter(18.0, -2.0, 0.0)
sphereSource6.SetRadius(6.0)

sphereMapper1 = vtk.vtkPolyDataMapper()
sphereMapper1.SetInputConnection(sphereSource1.GetOutputPort())

sphereMapper2 = vtk.vtkPolyDataMapper()
sphereMapper2.SetInputConnection(sphereSource2.GetOutputPort())

sphereMapper3 = vtk.vtkPolyDataMapper()
sphereMapper3.SetInputConnection(sphereSource3.GetOutputPort())

sphereMapper4 = vtk.vtkPolyDataMapper()
sphereMapper4.SetInputConnection(sphereSource4.GetOutputPort())

sphereMapper5 = vtk.vtkPolyDataMapper()
sphereMapper5.SetInputConnection(sphereSource5.GetOutputPort())

sphereMapper6 = vtk.vtkPolyDataMapper()
sphereMapper6.SetInputConnection(sphereSource6.GetOutputPort())

sphereActor1 = vtk.vtkActor()
sphereActor1.SetMapper(sphereMapper1)

sphereActor2 = vtk.vtkActor()
sphereActor2.SetMapper(sphereMapper2)

sphereActor3 = vtk.vtkActor()
sphereActor3.SetMapper(sphereMapper3)

sphereActor4 = vtk.vtkActor()
sphereActor4.SetMapper(sphereMapper4)

sphereActor5 = vtk.vtkActor()
sphereActor5.SetMapper(sphereMapper5)

sphereActor6 = vtk.vtkActor()
sphereActor6.SetMapper(sphereMapper6)

renderer.AddActor(sphereActor1)
renderer.AddActor(sphereActor2)
renderer.AddActor(sphereActor3)
renderer.AddActor(sphereActor4)
renderer.AddActor(sphereActor5)
renderer.AddActor(sphereActor6)

interactor.Initialize()
interactor.Start()

