
<!-- Improved compatibility of back to top link: See: https://github.com/molro/backend/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <h3 align="center">FastAPI - Ejemplo de Uso con Entornos virtuales de Python</h3>

  <p align="center">
    🎯 Desarrollo de Python con entornos virtuales
    <br />
    <a href="https://github.com/mouredev/Hello-Python/"><strong>Archivos »</strong></a>
    <br />
    <a href="https://github.com/mouredev/Hello-Python/issues">Reportar un bug</a>
    ·
    <a href="https://github.com/mouredev/Hello-Python/issues">Asignar una feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<!-- <details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installing </a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details> -->



<!-- ABOUT THE PROJECT -->
## Introducción

Por defecto la instalación de Python, incluye una gran cantidad de librerías de manera nativa y por defecto en la instalación de Python. Sin embargo es habitual el uso de liberías de terceros, como en este caso FastAPI.

Para instalar y manejar paquetes, el módulo pip es la herramienta que nos permite instalar estas librerías de terceros, sin embargo esto lo realiza de manera global. 

Cuando compartimos el código, mediante un repositorio en GitHub por ejemplo, para poder ejecutar la aplicación deberemos instalar todas aquellas librerías de terceros que hemos instalado previamente de manera manual, con el riesgo que eso conlleva. 

Para ello existen dos alternativas:
* Usar contenedores (Docker por ejemplo)
* Usar Entornos virtuales 

Porqué?
* Tu tiempo es valioso y debes enfocarte en crear soluciones para resolver problemas que ayuden a otros.
* No deberías pasar tiempo instalando y desinstalando versiones de Python una y otra vez por cada proyecto.
* Deberías implementar el principio KISS para el resto de tu vida y esto es parte de ello :smile:


En este tutorial nos enfocaremos en el uso y desarrollo con entornos virtuales.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Backend

Para comenzar el backend esta creado con:

- [![Python][python-shield]][python-url]
- [![FastApi][fastAPI-shield]][fastAPI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Qué es un entorno virtual?

Es un directorio autocontenido, que en su interior contiene una instalación de python con la versión particular para ese proyecto. Nos permite instalar además librería de terceros.

Es decir, permite ejecutar un proyecto con python y sus librerías, al mismo tiempo que tenemos otro proyecto con versiones de python y/o librerías distintas, sin necesidad de instalar y desinstalar cada vez que cambiemos de proyecto.

### Ventajas

La principal ventaja que nos encontramos es que nos permiten la portabilidad de nuestras aplicaciones. Imagina que escribes código, subes al repositorio y un compañero continúa con el proyecto desde su ordenador. El deberá instalar las liberías necesarias, pero puede ocurrir que existan diferentes versiones disponibles, esto lo podemos simplificar con una técnica similar al package.json de NodeJs, técnica que veremos mas adelante.

Otra ventaja es la estandarización, tu y todos los desarrolladores que trabajéis sobre la aplicación utilizaréis las mismas versiones tanto del lenguaje y de las librerías.

### Global vs Entorno Virtual

Para poder explicar las diferencias, podemos apreciar la comparación entre ambas imagenes.
IMG1 GLOBAL 
IMG 2 LOCAL

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Primeros pasos 

Crear un entorno virtual es relativamente sencillo, para ello necesitaremos tener instalado:
* [![Python][python-shield]][python-url]
* [![Git][git-shield]][git-url]
* Tu IDE Favorito
### Pre requisitos

Cómo instalar alguna de las herramientas 
* Git 
  * macOS -> Homebrew package manager -> [Learn more here][gitMac]
    ```sh
      brew install git
    ```
  * Linux
    * Para distribuciones basadas en Debian/Ubuntu
      ```sh
        apt-get install git
      ```
    * Basadas en Fedora
      ```sh
        yum install git
      ```
    Otras distribuciones [Download Git for Linux/Unix][gitLinux]

  * Windows

    La última versión de 32bit se puede descargar [Click Here][gitWindows32bit]<br/>
    Para otras descargas, puedes hacerlo desde [Dowload git for Windows][gitWindows]

* Python 
  * macOS 

    * Última versión [here][pylatestmacos]
    * Otras versiones [here][pymacos]

  * Windows  
    * Última versión [here][pylatestwin]
    * Otras versiones [here][pywin]
  
  * Linux/Unix 
  
    * GZipped source tarball [here][pygzip]
    * XZ source tarball [here][pyxz]
### Creando Entornos Virtuales 

IMPORTANTE!!! Trabajaremos sobre la terminal.

1. Clonamos el repositorio
   ```sh
   git clone https://github.com/mouredev/Hello-Python.git
   ```

2. Nos ubicamos en el directorio donde esta el backend

   ``` sh 
   cd /Hello-Python/Backend/FasAPI/
   ```
3. Comprobamos la versión de Python, en mi caso tengo la versión 3.10

   ``` sh
   python3 --version 
   ```
4. Comprobamos las liberías y versiones instaladas, con alguno de los comandos. 

    ``` sh
    python3 -m pip list
    ```
    ``` sh
    pip list
    ```
    ``` sh
    pip freeze
    ```
    Veremos como resultado todas las librerías instaladas y sus respectivas versiones.

5. Creamos nuestro entorno virtual, para ello utilizaremos la siguiente sintaxis

    ``` sh
    python3 -m venv NOMBRE_DIRECTORIO_VIRTUAL
    ```
    Ejecutamos el comando para crear un directorio llamado venv (De esta manera automáticamente se incluira en el git ignore, puedes llamarlo como desees, pero deberás incluir el directorio manualmente dentro del archivo .gitignore)
    
    ``` sh
    python3 -m venv venv
    ```
    Esto nos creará un directorio donde se instalará todo lo que necesitemos para el proyecto.
6. Para activar el entorno virtual necesitaremos activarlo mediante el siguiente comando:
    ```sh
    source NOMBRE_DIRECTORIO_VIRTUAL/bin/activate
    ```
    En nuestro caso utilizaremos el siguiente comando
    ```sh
    source venv/bin/activate
    ```

    Para desactivar utilizamos 
    ``` sh 
    deactivate
    ```
  <!-- IMAGEN DE ENTORNO VIRTUAL -->
7. Repetimos el paso 4 y comprobamos las versiones instaladas (Dentro del entorno virtual)
8. Instalamos las librerías utilizadas en el proyecto (Dentro del entorno virtual):
    
    ``` sh
    pip install "fastapi[all]"
    ```
9. Volvemos a repetir el paso 4 y comprobamos las versiones instaladas (Dentro del entorno virtual).

    Podemos ver las diferencias 
<!-- IMAGENES -->

### Manejando e instalando librerías

En este caso puede parecer sencillo instalar todas las librerías que necesitamos, ya que solo nos bastaría con el comando ```pip install "fastapi[all]" ```, pero sin embargo es probable que otros proyectos mas grandes requieran mas librerías y trabajar con versiones específicas.

A diferencia de otras tecnologías como NodeJS, que maneja sus paquetes y versiones mediante el archivo ```package.json``` que se crea una vez que inicializamos un proyecto. En python deberemos hacerlo de manera manual, lo haremos mediante la creación del archivo ```requirements.txt``` lo haremos siempre dentro del entorno virtual, podemos hacerlo en los siguientes pasos:
#### Crear requirements.txt
1. Para crear el archivo ```requirements.txt```
    ```sh
    python3 -m pip freeze > requirements.txt
    ```
    Si recordamos ```pip freeze``` nos permitía ver todas las librerías instaladas. Al utilizar ```>``` le estamos diciendo, el resultado de ```python3 -m pip freeze``` sácalo en ```requirements.txt```.

2. Si abrimos el archivo ```requirements.txt``` veremos todas librerías y versiones de python utilizadas en el proyecto.

* IMPORTANTE!!!! Si ejecutamos estos comandos, fuera del entorno virtual nos recopilará <b>todas</b> las librerías en nuestro ordenador de manera global.
Puedes probarlo para ver las diferencias entre instalación *Global vs Entorno Virtual*

#### Instalar con requirements.txt
1. Para instalar necesitaremos tener el archivo ```requirements.txt```en la raíz del proyecto y tener activado el entorno virtual.
    ```sh
    python3 -m pip install -r requirements.txt
    ```
    Este comenzará a instalar todas las dependencias dentro de nuestro entorno virtual.
2. Una vez finalizada podemos comprobar, con 
    ``` sh
    python3 -m pip list
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Creado bajo licencia Apache-2.0 visita aquí para mas información [licencia][license-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[![Twitter][twitter-shield]][twitter-url] [![GitHub][github-shield]][github-url]<br/>
Project Link: [Hello-Python](https://github.com/mouredev/Hello-Python/tree/main/Backend/FastAPI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Python Tools -->
[python-shield]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org

[fastAPI-shield]:https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[fastAPI-url]:https://fastapi.tiangolo.com
<!-- Git -->
[git-shield]:https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-url]: https://git-scm.com
<!-- Python -->
[pylatestmacos]:https://www.python.org/downloads/release/python-3111/
[pymacos]:https://www.python.org/downloads/macos/

[pylatestwin]:https://www.python.org/downloads/release/python-3111/
[pywin]:https://www.python.org/downloads/windows/

[pygzip]:https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
[pyxz]:https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz

[pywindowsdockermac-url]:https://docs.docker.com/desktop/install/mac-install/
<!-- Redes  -->
[twitter-shield]:https://img.shields.io/twitter/follow/molro?style=social
[twitter-url]:https://www.twitter.com/molro
[github-shield]:https://img.shields.io/github/followers/molro?style=social
[github-url]: https://github.com/molro/

[license-url]:https://github.com/mouredev/Hello-Python/blob/main/LICENSE