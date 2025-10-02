from __future__ import annotations
import meshlib.mrmeshpy
import numpy
import typing
import typing_extensions
__all__: list[str] = ['edgeBitSetFromBools', 'faceBitSetFromBools', 'fromNumpyArray', 'getNumpy3Darray', 'getNumpyBitSet', 'getNumpyCurvature', 'getNumpyFaces', 'getNumpyGaussianCurvature', 'getNumpyMeanCurvature', 'getNumpyVerts', 'meshFromFacesVerts', 'meshFromUVPoints', 'pointCloudFromPoints', 'polyline2FromPoints', 'simpleVolumeFrom3Darray', 'toNumpyArray', 'undirectedEdgeBitSetFromBools', 'vertBitSetFromBools']
def edgeBitSetFromBools(boolArray: typing_extensions.Buffer) -> meshlib.mrmeshpy.EdgeBitSet:
    """
    returns EdgeBitSet from numpy array with bools
    """
def faceBitSetFromBools(boolArray: typing_extensions.Buffer) -> meshlib.mrmeshpy.FaceBitSet:
    """
    returns FaceBitSet from numpy array with bools
    """
def fromNumpyArray(coords: typing_extensions.Buffer) -> meshlib.mrmeshpy.std_vector_Vector3_float:
    """
    constructs mrmeshpy.vectorVector3f from numpy ndarray with shape (n,3)
    """
def getNumpy3Darray(simpleVolume: meshlib.mrmeshpy.SimpleVolume) -> numpy.ndarray[numpy.float64]:
    """
    Convert SimpleVolume to numpy 3D array
    """
def getNumpyBitSet(bitset: meshlib.mrmeshpy.BitSet) -> numpy.ndarray[bool]:
    """
    returns numpy array with bools for each bit of given bitset
    """
def getNumpyCurvature(mesh: meshlib.mrmeshpy.Mesh) -> numpy.ndarray[numpy.float64]:
    """
    retunrs numpy array with discrete mean curvature for each vertex of a mesh
    """
def getNumpyFaces(topology: meshlib.mrmeshpy.MeshTopology) -> numpy.ndarray[numpy.int32]:
    """
    returns numpy array shapes [num faces,3] which represents vertices of mesh valid faces 
    """
def getNumpyGaussianCurvature(mesh: meshlib.mrmeshpy.Mesh) -> numpy.ndarray[numpy.float64]:
    """
    retunrs numpy array with discrete Gaussian curvature for each vertex of a mesh
    """
def getNumpyMeanCurvature(mesh: meshlib.mrmeshpy.Mesh) -> numpy.ndarray[numpy.float64]:
    """
    retunrs numpy array with discrete mean curvature for each vertex of a mesh
    """
def getNumpyVerts(mesh: meshlib.mrmeshpy.Mesh) -> numpy.ndarray[numpy.float64]:
    """
    returns numpy array shapes [num verts,3] which represents coordinates of all mesh points (including invalid ones)
    """
def meshFromFacesVerts(faces: typing_extensions.Buffer, verts: typing_extensions.Buffer, settings: meshlib.mrmeshpy.MeshBuilder.BuildSettings = ..., duplicateNonManifoldVertices: bool = True) -> meshlib.mrmeshpy.Mesh:
    """
    constructs mesh from given numpy ndarrays of faces (N VertId x3, FaceId x1), verts (M vec3 x3)
    """
def meshFromUVPoints(xArray: typing_extensions.Buffer, yArray: typing_extensions.Buffer, zArray: typing_extensions.Buffer) -> meshlib.mrmeshpy.Mesh:
    """
    constructs mesh from three 2d numpy ndarrays with x,y,z positions of mesh
    """
def pointCloudFromPoints(points: typing_extensions.Buffer, normals: typing_extensions.Buffer = ...) -> meshlib.mrmeshpy.PointCloud:
    """
    creates point cloud object from numpy arrays, first arg - points, second optional arg - normals
    """
def polyline2FromPoints(points: typing_extensions.Buffer) -> meshlib.mrmeshpy.Polyline2:
    """
    creates polyline2 object from numpy array
    """
def simpleVolumeFrom3Darray(3DvoxelsArray: typing_extensions.Buffer) -> meshlib.mrmeshpy.SimpleVolumeMinMax:
    """
    Convert numpy 3D array to SimpleVolume
    """
@typing.overload
def toNumpyArray(coords: meshlib.mrmeshpy.VertCoords) -> numpy.ndarray[numpy.float64]:
    """
    returns numpy array shapes [num coords,3] which represents coordinates from given vector
    """
@typing.overload
def toNumpyArray(coords: meshlib.mrmeshpy.FaceNormals) -> numpy.ndarray[numpy.float64]:
    """
    returns numpy array shapes [num coords,3] which represents coordinates from given vector
    """
@typing.overload
def toNumpyArray(coords: meshlib.mrmeshpy.std_vector_Vector3_float) -> numpy.ndarray[numpy.float64]:
    """
    returns numpy array shapes [num coords,3] which represents coordinates from given vector
    """
def undirectedEdgeBitSetFromBools(boolArray: typing_extensions.Buffer) -> meshlib.mrmeshpy.UndirectedEdgeBitSet:
    """
    returns UndirectedEdgeBitSet from numpy array with bools
    """
def vertBitSetFromBools(boolArray: typing_extensions.Buffer) -> meshlib.mrmeshpy.VertBitSet:
    """
    returns VertBitSet from numpy array with bools
    """
