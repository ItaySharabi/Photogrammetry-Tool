# MicMac Photogrammetry tools - Automated!

<a href="https://micmac.ensg.eu/index.php/Accueil"> MicMac </a> is a free open-source photogrammetric suite that can be used in a variety of 3D reconstruction scenarios. MicMac aims mainly at professionnal or academic users but constant efforts are made to make it more accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be used in various fields: cartography, environment, industry, forestry, heritage, archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when appropriate.


<p>
  <h1 align="center">~ Simple MicMac ~</h1>
</p>

## Simplifying MicMac tools
The goal is to create a `Facade` software, which will be easy to use, such that running a single executable,
or, running a single command in the command-line will produce some photogrammetric artifact.

MicMac made this software accomplishable by implementing photogrammetric tools not through GUI, but through the command-line.

<p>
  <h1 align="center">How to install and run this tool</h1>
</p>

<a href="https://micmac.ensg.eu/index.php/Install_MicMac_Windows">MicMac installation guide</a>
<br>

1. Download <a href="https://github.com/micmacIGN/micmac/releases">MicMac binaries</a>.

2. Add a new environemental variable: for example D:\MicMac\bin

3. Run our `setup_win64.py` file. It will fix any Windows permission error, while saving your pervious permissions (ACL).

4. Run `SimpleMicMac.py` with an image directory path and a model name!

Example: `python3 SimpleMicMac.py TestDataset/.*.JPG TestModelName`

This command will directly offer you some photogrammetry methods to apply to your given dataset!


# Try your own dataset:

Testing our very small dataset on MicMac tools have produced the following results: 

### (<a href="https://github.com/ItaySharabi/Auto-Photogrammetry-Tool/tree/master/TestDataset">Statue dataset</a>)

<span>
  
<img src="https://user-images.githubusercontent.com/63110245/173765942-bce9a4b1-09a8-46f4-bc07-920deca9f297.png" width=400 height=300>

<img src="https://user-images.githubusercontent.com/63110245/173765329-67fd1af9-58b9-43e3-9b6a-b83b97d4e859.png" width=400 height=300>
  
</span>

Around 10-12 images of this statue have produced the following result:

<br>
A very low resolution point cloud (Low data volume - high noise):

![statue](https://user-images.githubusercontent.com/63110245/173766653-d33947b5-33fa-4156-8473-4a24f4c604d4.jpeg)

