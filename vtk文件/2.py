import vtk

# Sphere
sphereSource1 = vtk.vtkSphereSource()
sphereSource1.SetCenter(-13.0, 0.0, 0.0)
sphereSource1.SetRadius(3.0)

sphereSource2 = vtk.vtkSphereSource()
sphereSource2.SetCenter(-4.0, 0.0, 0.0)
sphereSource2.SetRadius(4.0)


sphereSource3 = vtk.vtkSphereSource()
sphereSource3.SetCenter(4.0, 0.0, 0.0)
sphereSource3.SetRadius(4.0)

sphereSource4 = vtk.vtkSphereSource()
sphereSource4.SetCenter(13.0, 0.0, 0.0)
sphereSource4.SetRadius(3.0)


sphereMapper1 = vtk.vtkPolyDataMapper()
sphereMapper1.SetInputConnection(sphereSource1.GetOutputPort())

sphereMapper2 = vtk.vtkPolyDataMapper()
sphereMapper2.SetInputConnection(sphereSource2.GetOutputPort())


sphereMapper3 = vtk.vtkPolyDataMapper()
sphereMapper3.SetInputConnection(sphereSource3.GetOutputPort())

sphereMapper4 = vtk.vtkPolyDataMapper()
sphereMapper4.SetInputConnection(sphereSource4.GetOutputPort())



sphereActor1 = vtk.vtkActor()
sphereActor1.SetMapper(sphereMapper1)

sphereActor2 = vtk.vtkActor()
sphereActor2.SetMapper(sphereMapper2)


sphereActor3 = vtk.vtkActor()
sphereActor3.SetMapper(sphereMapper3)

sphereActor4 = vtk.vtkActor()
sphereActor4.SetMapper(sphereMapper4)


ren1=vtk.vtkRenderer()
ren2=vtk.vtkRenderer()
ren1.AddActor(sphereActor1)
ren1.AddActor(sphereActor2)
ren2.AddActor(sphereActor3)
ren2.AddActor(sphereActor4)


ren1.SetBackground(0.2,0.4,0.4)
ren1.SetViewport(0.0,0.0,0.5,1.0)
ren2.SetBackground(0.5,0.6,0.5)
ren2.SetViewport(0.5,0.0,1.0,1.0)
renWin=vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.AddRenderer(ren2)
renWin.SetSize(600,600)
renWin.Render()
iren=vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()

