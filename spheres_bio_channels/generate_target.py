import gmsh
import sys

# Get command line arguments (skip the script name)
args = sys.argv[1:]

# Parse arguments into sphere positions
sphere_positions = []
for i in range(0, len(args), 3):
    y = float(args[i])
    x = -float(args[i+1])
    z = -float(args[i+2])
    sphere_positions.append((x, y, z))


# Define variables for sphere positions and dimensions
sphere_radius = 0.85  # Radius of the hollow chambers (in mm)
tube_radius = 0.35    # Radius of the tubes (in mm, half the diameter)
radius = 0.5         # Radius of the spheres (the real objects)



# Print the sphere positions
print("Sphere positions:", sphere_positions)


# Initialize gmsh
gmsh.initialize()

# Create a new model
gmsh.model.add("simple_cylinder")


gmsh.option.setNumber("Mesh.MeshSizeMin", 0.05)  # Decrease for finer details
gmsh.option.setNumber("Mesh.MeshSizeMax", 0.1)  # Decrease for finer details


# Create cylinder (height = 10mm, radius = 5mm)
# Parameters: x, y, z (center of base), dx, dy, dz (axis vector), radius
cylinder = gmsh.model.occ.addBox(-5.0, -5.0, -5.0, 10, 10, 10)

# Synchronize the model
gmsh.model.occ.synchronize()

# Set mesh size parameters
gmsh.option.setNumber("Mesh.MeshSizeMin", 0.5)  # Minimum element size
gmsh.option.setNumber("Mesh.MeshSizeMax", 1.0)  # Maximum element size

# Generate 3D mesh
gmsh.model.mesh.generate(3)

# Save the mesh in STL format
gmsh.write("simple_cylinder.stl")


# Finalize gmsh
gmsh.finalize()

print("Cylinder mesh created successfully!")




import gmsh
import sys



# Initialize gmsh
gmsh.initialize()

gmsh.option.setNumber("Mesh.MeshSizeMin", 0.05)  # Decrease for finer details
gmsh.option.setNumber("Mesh.MeshSizeMax", 0.1)  # Decrease for finer details

# Create a new model
gmsh.model.add("outer_hull")




# Create spheres
spheres = []
for pos in sphere_positions:
    spheres.append(gmsh.model.occ.addSphere(*pos, sphere_radius))

# Create cylinders (tubes) connecting the spheres
cylinders = []


cylinders.append(gmsh.model.occ.addCylinder(0,0,-2.2 - 1,
                                            0,
                                            0,
                                            1,
                                            0.6))


cylinders.append(gmsh.model.occ.addCylinder(*sphere_positions[0],
                                            0 - sphere_positions[0][0],
                                            0 - sphere_positions[0][1],
                                            -2.5 - sphere_positions[0][2],
                                            tube_radius))

cylinders.append(gmsh.model.occ.addCylinder(*sphere_positions[0],
                                            sphere_positions[1][0] - sphere_positions[0][0],
                                            sphere_positions[1][1] - sphere_positions[0][1],
                                            sphere_positions[1][2] - sphere_positions[0][2],
                                            tube_radius))

cylinders.append(gmsh.model.occ.addCylinder(*sphere_positions[1],
                                            0 - sphere_positions[1][0],
                                            0 - sphere_positions[1][1],
                                            2.5 - sphere_positions[1][2],
                                            tube_radius))

cylinders.append(gmsh.model.occ.addCylinder(0,0,2.2,
                                            0 - 0,
                                            0,
                                            1,
                                            0.6))


# Synchronize the model
gmsh.model.occ.synchronize()

# Perform a Boolean union (fuse) to merge all shapes into a single outer hull
# This removes all internal structures
all_entities = [(3, s) for s in spheres] + [(3, c) for c in cylinders]
fused_entities, _ = gmsh.model.occ.fuse(all_entities, all_entities)
gmsh.model.occ.synchronize()

# Generate a 2D surface mesh (hull only)
gmsh.model.mesh.generate(2)

# Save the surface mesh to a file
gmsh.write("triangle.stl")

# Finalize gmsh
gmsh.finalize()


import trimesh
import numpy as np

# Load the two meshes
triangle_mesh = trimesh.load('triangle.stl')
cylinder_mesh = trimesh.load('simple_cylinder.stl')

print(f"Loaded triangle mesh with {len(triangle_mesh.vertices)} vertices and {len(triangle_mesh.faces)} faces")
print(f"Loaded cylinder mesh with {len(cylinder_mesh.vertices)} vertices and {len(cylinder_mesh.faces)} faces")

# Simply combine the meshes without merging
# This creates a scene with both meshes
#scene = trimesh.util.concatenate([triangle_mesh, cylinder_mesh])
scene = trimesh.boolean.union([cylinder_mesh, triangle_mesh])

# Export the combined meshes as a single PLY file
# The as_mesh() function combines the meshes in the scene into a single mesh
#combined_mesh = scene.to_mesh()

# Save the combined mesh as PLY
scene.export('final.ply')
scene.export('final.stl')


import numpy as np
import os

# First, export the meshes in a format that OpenSCAD can read
# (assuming you already have the meshes loaded)
triangle_mesh.export('triangle_for_openscad.stl')
cylinder_mesh.export('cylinder_for_openscad.stl')

# Create an OpenSCAD script to perform the boolean operation
with open('boolean_operation.scad', 'w') as f:
    f.write('''
    difference() {
        import("cylinder_for_openscad.stl");
        import("triangle_for_openscad.stl");
    }
    ''')

# Run OpenSCAD to generate the result
# Path to OpenSCAD
openscad_path = r"C:\Program Files\OpenSCAD\openscad.com"

# Example: Render an OpenSCAD file to STL
scad_file = "boolean_operation.scad"
output_file = "final.stl"

import subprocess
# Call OpenSCAD
subprocess.run([openscad_path, "-o", output_file, scad_file])
print(f"OpenSCAD operation completed. Check final.stl")

print(f"Convert to .ply")
import pymeshlab

# Load the PLY file
ms = pymeshlab.MeshSet()
ms.load_new_mesh('final.stl')
# Save as STL file
ms.save_current_mesh('final.ply')







# Initialize gmsh
gmsh.initialize()
# Create a new model
gmsh.model.add("Sphere")
# Create sphere with center at position and radius 3mm
x, y, z = sphere_positions[0]
sphere_tag = gmsh.model.occ.addSphere(x, y, z, radius)
# Synchronize the model
gmsh.model.occ.synchronize()
# Generate mesh
gmsh.model.mesh.generate(3)
# Write to STL file
gmsh.write("sphere1.stl")
# Finalize gmsh
gmsh.finalize()
# Load the PLY file
ms = pymeshlab.MeshSet()
ms.load_new_mesh('sphere1.stl')
# Save as STL file
ms.save_current_mesh('sphere1.ply')



# Initialize gmsh
gmsh.initialize()
# Create a new model
gmsh.model.add("Sphere")
# Create sphere with center at position and radius 3mm
x, y, z = sphere_positions[1]
sphere_tag = gmsh.model.occ.addSphere(x, y, z, radius)
# Synchronize the model
gmsh.model.occ.synchronize()
# Generate mesh
gmsh.model.mesh.generate(3)
# Write to STL file
gmsh.write("sphere2.stl")
# Finalize gmsh
gmsh.finalize()
# Load the PLY file
ms = pymeshlab.MeshSet()
ms.load_new_mesh('sphere2.stl')
# Save as STL file
ms.save_current_mesh('sphere2.ply')

