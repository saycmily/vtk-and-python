import vtk

from vtk.util.colors import grey

class MyInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self,parent=None):
        self.parent = iren

        self.AddObserver("KeyPressEvent",self.keyPressEvent)

    def keyPressEvent(self,obj,event):
        key = self.parent.GetKeySym()
        if key == 'Up':
            r = vtk.vtkMath.Random(0.1, 1.0)
            g = vtk.vtkMath.Random(0.1, 1.0)
            b = vtk.vtkMath.Random(0.1, 1.0)
            cubeActor.GetProperty().SetColor(r, g, b)
            renWin.Render()


cube = vtk.vtkSphereSource()
cube.SetCenter(0.0,0.0,0.0)
cube.SetRadius(1.0)
cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())

cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetColor(grey)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()

iren.SetInteractorStyle(MyInteractorStyle())

iren.SetRenderWindow(renWin)

ren.AddActor(cubeActor)
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(600, 600)

iren.Initialize()

ren.ResetCamera()
ren.GetActiveCamera().Zoom(0.6)
renWin.Render()

iren.Start()