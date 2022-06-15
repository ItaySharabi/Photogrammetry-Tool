# MicMac Photogrammetry tools - Automated!

<a href="https://micmac.ensg.eu/index.php/Accueil"> MicMac </a> is a free open-source photogrammetric suite that can be used in a variety of 3D reconstruction scenarios. MicMac aims mainly at professionnal or academic users but constant efforts are made to make it more accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be used in various fields : cartography, environment, industry, forestry, heritage, archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when appropriate.


<p>
  <h1 align="center">~ Simple MicMac ~</h1>
</p>

## Simplifying MicMac tools
The goal is to create a `Facade` software, which will be easy to use, such as running a single executable,
or, running a single command in the command-line.

MicMac made this software accomplishable by implementing photogrammetric tools not through GUI, but through the command-line.

<p>
  <h1 align="center">How to install and run this tool</h1>
</p>

<a href="https://micmac.ensg.eu/index.php/Install_MicMac_Windows">MicMac installation guide</a>
<br>

1. Download <a href="https://github.com/micmacIGN/micmac/releases">MicMac binaries</a>.

2. Add a new environnemental variable (Screenshot 3) : for example D:\MicMac\bin

3. Run our `setup_win64.py` file. It will fix and Windows permission error, while saving your pervious permissions.

4. Run `SimpleMicMac.py` with an image directory path and a model name!

Example: `python3 SimpleMicMac.py TestDataset/.*.JPG TestModelName`

This command will directly offer you some photogrammetry methods to apply to your given dataset!


