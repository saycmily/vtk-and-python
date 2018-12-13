# coding = utf-8
import vtk

# 存储空间点
points = vtk.vtkPoints()
# 存储空间面片
CellArray = vtk.vtkCellArray()

# 加入空间点
points.SetNumberOfPoints(4)
points.SetPoint(0, (0,0,0))
points.SetPoint(1, (0,1,0))
points.SetPoint(2, (1,1,0))
points.SetPoint(3, (1,0,0))

# 加入形成当前面片的点的个数
CellArray.InsertNextCell(3)
# 分别将先前定义的点的序号加入进去
CellArray.InsertCellPoint(0)
CellArray.InsertCellPoint(1)
CellArray.InsertCellPoint(2)
CellArray.InsertCellPoint(3)

aRenderer = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()

renWin.AddRenderer(aRenderer)
iren.SetRenderWindow(renWin)

sur = vtk.vtkPolyData()
sur.SetPoints(points)
sur.SetPolys(CellArray)

mapper1 = vtk.vtkPolyDataMapper()

if vtk.VTK_MAJOR_VERSION <= 5:
    mapper1.SetInput(sur)
else:
    mapper1.SetInputData(sur)

Actor = vtk.vtkActor()
Actor.SetMapper(mapper1)
Actor.GetProperty().SetDiffuseColor(1, 0, 0)
Actor.GetProperty().SetSpecular(.5)
Actor.GetProperty().SetSpecularPower(30)

aRenderer.AddActor(Actor)
aRenderer.SetBackground(.6, .8, .8)
renWin.SetSize(600, 600)
aRenderer.ResetCameraClippingRange()
iren.Initialize()
iren.Start()