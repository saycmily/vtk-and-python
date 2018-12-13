# coding = gbk
import vtk


class Vertebra:

    def __init__(self):
        self.size = 1
        self.height = 6
        self.distance = 2
        self.position = [0, 0, 0]
        self.points = vtk.vtkPoints()
        self.CellArray = vtk.vtkCellArray()
        self.surface = vtk.vtkPolyData()

    def setParams(self, size, height, distance, position):
        self.size = size
        self.height = height
        self.distance = distance
        self.position = position

    def Initialize(self):
        p1 = self.position[0]
        p2 = self.position[1]
        p3 = self.position[2]
        h1 = self.height
        h2 = self.height / 2
        h3 = self.height / 3
        h4 = h3 * 2

        self.points.SetNumberOfPoints(31)
        self.points.SetPoint(0, (p1, p2, p3))
        self.points.SetPoint(1, ((p1 - 2) * self.size, (p2 - 2) * self.size, p3 + h2))
        self.points.SetPoint(2, ((p1 - 0) * self.size, (p2 - 4) * self.size, p3 + h2))
        self.points.SetPoint(3, ((p1 + 2) * self.size, (p2 - 2) * self.size, p3 + h2))
        self.points.SetPoint(4, ((p1 - 0) * self.size, (p2 + 8) * self.size, p3))
        self.points.SetPoint(5, ((p1 - 4) * self.size, (p2 + 6) * self.size, p3))
        self.points.SetPoint(6, ((p1 - 6) * self.size, (p2 + 1) * self.size, p3))
        self.points.SetPoint(7, ((p1 - 4) * self.size, (p2 - 2) * self.size, p3 + h3))
        self.points.SetPoint(8, ((p1 - 8) * self.size, (p2 - 8) * self.size, p3 + h2))
        self.points.SetPoint(9, ((p1 - 2) * self.size, (p2 - 5) * self.size, p3 + h2))
        self.points.SetPoint(10, ((p1 + 2) * self.size, (p2 - 5) * self.size, p3 + h2))
        self.points.SetPoint(11, ((p1 + 8) * self.size, (p2 - 8) * self.size, p3 + h2))
        self.points.SetPoint(12, ((p1 + 4) * self.size, (p2 - 2) * self.size, p3 + h3))
        self.points.SetPoint(13, ((p1 + 6) * self.size, (p2 + 1) * self.size, p3))
        self.points.SetPoint(14, ((p1 + 4) * self.size, (p2 + 6) * self.size, p3))
        self.points.SetPoint(15, (p1, p2, p3 + h1))
        self.points.SetPoint(16, ((p1 - 2) * self.size, (p2 - 2) * self.size, p3 + 2 * h4))
        self.points.SetPoint(17, ((p1 - 0) * self.size, (p2 - 4) * self.size, p3 + h1))
        self.points.SetPoint(18, ((p1 + 2) * self.size, (p2 - 2) * self.size, p3 + 2 * h4))
        self.points.SetPoint(19, (p1 * self.size, (p2 + 8) * self.size, p3 + h1))
        self.points.SetPoint(20, ((p1 - 4) * self.size, (p2 + 6) * self.size, p3 + h1))
        self.points.SetPoint(21, ((p1 - 6) * self.size, (p2 + 1) * self.size, p3 + h1))
        self.points.SetPoint(22, ((p1 - 4) * self.size, (p2 - 2) * self.size, p3 + h4))
        self.points.SetPoint(23, ((p1 - 8) * self.size, (p2 - 8) * self.size, p3 + h1))
        self.points.SetPoint(24, ((p1 - 2) * self.size, (p2 - 5) * self.size, p3 + h1))
        self.points.SetPoint(25, ((p1 + 2) * self.size, (p2 - 5) * self.size, p3 + h1))
        self.points.SetPoint(26, ((p1 + 8) * self.size, (p2 - 8) * self.size, p3 + h1))
        self.points.SetPoint(27, ((p1 + 4) * self.size, (p2 - 2) * self.size, p3 + h4))
        self.points.SetPoint(28, ((p1 + 6) * self.size, (p2 + 1) * self.size, p3 + h1))
        self.points.SetPoint(29, ((p1 + 4) * self.size, (p2 + 6) * self.size, p3 + h1))
        self.points.SetPoint(30, (p1, (p1 - 12) * self.size, p3 - h4))

        self.CellArray.InsertNextCell(6)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(6)
        self.CellArray.InsertCellPoint(5)
        self.CellArray.InsertCellPoint(4)
        self.CellArray.InsertCellPoint(14)
        self.CellArray.InsertCellPoint(13)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(6)
        self.CellArray.InsertCellPoint(7)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(7)
        self.CellArray.InsertCellPoint(1)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(1)
        self.CellArray.InsertCellPoint(7)
        self.CellArray.InsertCellPoint(9)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(1)
        self.CellArray.InsertCellPoint(9)
        self.CellArray.InsertCellPoint(2)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(7)
        self.CellArray.InsertCellPoint(8)
        self.CellArray.InsertCellPoint(9)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(2)
        self.CellArray.InsertCellPoint(9)
        self.CellArray.InsertCellPoint(10)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(7)
        self.CellArray.InsertCellPoint(8)
        self.CellArray.InsertCellPoint(9)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(12)
        self.CellArray.InsertCellPoint(13)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(3)
        self.CellArray.InsertCellPoint(12)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(3)
        self.CellArray.InsertCellPoint(2)
        self.CellArray.InsertCellPoint(10)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(3)
        self.CellArray.InsertCellPoint(10)
        self.CellArray.InsertCellPoint(12)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(12)
        self.CellArray.InsertCellPoint(10)
        self.CellArray.InsertCellPoint(11)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(4)
        self.CellArray.InsertCellPoint(5)
        self.CellArray.InsertCellPoint(20)
        self.CellArray.InsertCellPoint(19)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(5)
        self.CellArray.InsertCellPoint(6)
        self.CellArray.InsertCellPoint(21)
        self.CellArray.InsertCellPoint(20)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(6)
        self.CellArray.InsertCellPoint(7)
        self.CellArray.InsertCellPoint(22)
        self.CellArray.InsertCellPoint(21)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(7)
        self.CellArray.InsertCellPoint(8)
        self.CellArray.InsertCellPoint(23)
        self.CellArray.InsertCellPoint(22)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(8)
        self.CellArray.InsertCellPoint(9)
        self.CellArray.InsertCellPoint(24)
        self.CellArray.InsertCellPoint(23)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(10)
        self.CellArray.InsertCellPoint(11)
        self.CellArray.InsertCellPoint(26)
        self.CellArray.InsertCellPoint(25)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(11)
        self.CellArray.InsertCellPoint(12)
        self.CellArray.InsertCellPoint(27)
        self.CellArray.InsertCellPoint(26)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(12)
        self.CellArray.InsertCellPoint(13)
        self.CellArray.InsertCellPoint(28)
        self.CellArray.InsertCellPoint(27)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(13)
        self.CellArray.InsertCellPoint(14)
        self.CellArray.InsertCellPoint(29)
        self.CellArray.InsertCellPoint(28)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(14)
        self.CellArray.InsertCellPoint(4)
        self.CellArray.InsertCellPoint(19)
        self.CellArray.InsertCellPoint(29)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(1)
        self.CellArray.InsertCellPoint(16)
        self.CellArray.InsertCellPoint(15)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(1)
        self.CellArray.InsertCellPoint(2)
        self.CellArray.InsertCellPoint(17)
        self.CellArray.InsertCellPoint(16)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(2)
        self.CellArray.InsertCellPoint(3)
        self.CellArray.InsertCellPoint(18)
        self.CellArray.InsertCellPoint(17)

        self.CellArray.InsertNextCell(4)
        self.CellArray.InsertCellPoint(3)
        self.CellArray.InsertCellPoint(0)
        self.CellArray.InsertCellPoint(15)
        self.CellArray.InsertCellPoint(18)

        self.CellArray.InsertNextCell(6)
        self.CellArray.InsertCellPoint(15)
        self.CellArray.InsertCellPoint(21)
        self.CellArray.InsertCellPoint(20)
        self.CellArray.InsertCellPoint(19)
        self.CellArray.InsertCellPoint(29)
        self.CellArray.InsertCellPoint(28)


        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(15)
        self.CellArray.InsertCellPoint(21)
        self.CellArray.InsertCellPoint(22)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(15)
        self.CellArray.InsertCellPoint(22)
        self.CellArray.InsertCellPoint(16)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(16)
        self.CellArray.InsertCellPoint(22)
        self.CellArray.InsertCellPoint(24)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(16)
        self.CellArray.InsertCellPoint(24)
        self.CellArray.InsertCellPoint(17)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(22)
        self.CellArray.InsertCellPoint(23)
        self.CellArray.InsertCellPoint(24)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(17)
        self.CellArray.InsertCellPoint(24)
        self.CellArray.InsertCellPoint(25)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(22)
        self.CellArray.InsertCellPoint(23)
        self.CellArray.InsertCellPoint(24)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(15)
        self.CellArray.InsertCellPoint(27)
        self.CellArray.InsertCellPoint(28)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(15)
        self.CellArray.InsertCellPoint(18)
        self.CellArray.InsertCellPoint(27)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(18)
        self.CellArray.InsertCellPoint(17)
        self.CellArray.InsertCellPoint(25)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(18)
        self.CellArray.InsertCellPoint(25)
        self.CellArray.InsertCellPoint(27)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(27)
        self.CellArray.InsertCellPoint(25)
        self.CellArray.InsertCellPoint(26)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(9)
        self.CellArray.InsertCellPoint(10)
        self.CellArray.InsertCellPoint(30)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(10)
        self.CellArray.InsertCellPoint(25)
        self.CellArray.InsertCellPoint(30)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(24)
        self.CellArray.InsertCellPoint(9)
        self.CellArray.InsertCellPoint(30)

        self.CellArray.InsertNextCell(3)
        self.CellArray.InsertCellPoint(24)
        self.CellArray.InsertCellPoint(25)
        self.CellArray.InsertCellPoint(30)

    def Draw(self):
        self.Initialize()

        aRenderer = vtk.vtkRenderer()
        renWin = vtk.vtkRenderWindow()
        iren = vtk.vtkRenderWindowInteractor()

        renWin.AddRenderer(aRenderer)
        iren.SetRenderWindow(renWin)

        sur = vtk.vtkPolyData()
        sur.SetPoints(self.points)
        sur.SetPolys(self.CellArray)

        map = vtk.vtkPolyDataMapper()
        if vtk.VTK_MAJOR_VERSION <= 5:
            map.SetInput(sur)
        else:
            map.SetInputData(sur)

        Actor = vtk.vtkActor()
        Actor.SetMapper(map)
        Actor.GetProperty().SetDiffuseColor(1, 0, 0)
        Actor.GetProperty().SetSpecular(.5)
        Actor.GetProperty().SetSpecularPower(30)
        Actor.SetPosition(self.position)

        aRenderer.AddActor(Actor)
        aRenderer.SetBackground(.6, .8, .8)
        renWin.SetSize(600, 600)
        aRenderer.ResetCameraClippingRange()
        iren.Initialize()
        iren.Start()

    def Output(self):
        self.Initialize()
        self.surface.SetPoints(self.points)
        self.surface.SetPolys(self.CellArray)
        a = vtk.vtkPolyData()

        return self.surface


if __name__ == '__main__':
    # Append the two meshes
    appendFilter = vtk.vtkAppendPolyData()

    for i in range(10):
        x1 = Vertebra()
        x1.setParams(3, 6, 2, [0,0,i*10])
        a = vtk.vtkPolyData()
        a.DeepCopy(x1.Output())
        appendFilter.AddInputData(a)

    appendFilter.Update()

    #  Remove any duplicate points.
    cleanFilter = vtk.vtkCleanPolyData()
    cleanFilter.SetInputConnection(appendFilter.GetOutputPort())
    cleanFilter.Update()

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cleanFilter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()

    renderWindow = vtk.vtkRenderWindow()

    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(.6, .8, .8)

    renderWindow.Render()
    renderWindow.SetSize(600, 600)
    renderWindowInteractor.Start()
