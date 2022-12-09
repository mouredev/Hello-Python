
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
    <a href="https://github.com/molro/backend"><strong>Archivos »</strong></a>
    <br />
    <a href="https://github.com/molro/backend/issues">Reportar un bug</a>
    ·
    <a href="https://github.com/molro/backend/issues">Asignar una feature</a>
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
## About 

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

### Qué es un entorno virtual?

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

Trabajaremos sobre la terminal.

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
    python3 -m venv NOMBRE DEL DIRECTORIO VIRTUAL
    ```
    Ejecutamos el comando para crear un directorio llamado venv (De esta manera automáticamente se incluira en el git ignore, puedes llamarlo como desees, pero deberás incluir el directorio manualmente dentro del archivo .gitignore)
    
    ``` sh
    python3 -m venv venv
    ```
    Esto nos creará un directorio donde se instalará todo lo que necesitemos para el proyecto.
6. Repetimos el paso 4 y comprobamos las versiones instaladas.
7. Instalamos las librerías utilizadas en el proyecto:
    
    ``` sh
    pip install "fastapi[all]"
    ```
8. Volvemos a repetir el paso 4 y comprobamos las versiones instaladas.

    Podemos ver las diferencias 
<!-- Pendiente Crear requirements -->
<!-- Pendiente Instalar librerías con requirements -->
3. Test the endpoints  

    Actually the backend has only two endpoints working
    
    1. GET ``` http://127.0.0.1:3009 ``` - Response status 200 and Json. The first time the reponse will be an empty array ```[] ``` 
    2. POST ``` http://127.0.0.1:3009/crear ``` - Response 200 and OK message and Post a preestablished message 
    ```sh
        {
        "_id": str,
        "tipo": "Usuario",
        "estado": "Feliz",
        "__v": 0
        }
    ``` 

4. Code!

    Write your code, make the API-REST growing up or connect with your frontend.

5. Testing your code
    - Running the application and review the changes
    ```sh
    docker compose up -d
    ```
    - Stop the application
    ```sh
      docker compose down
    ```

8. Add, Commit and Push! 
```sh
    git add . 
    git commit -m "Your Commit" 
    git push
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Creado bajo licencia Apache-2.0 visita aquí para mas información [licencia][license-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[![Twitter][twitter-shield]][twitter-url] [![GitHub][github-shield]][github-url]<br/>
Project Link: [https://github.com/molro/backend](https://github.com/molro/backend)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[python-shield]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org

[fastAPI-shield]:https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[fastAPI-url]:https://fastapi.tiangolo.com

[nodejs-shield]: https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[node-url]: https://nodejs.org/en/
[expressjs-shield]: https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB
[expressjs-url]: https://expressjs.com
[mongoDB-shield]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[mongoDB-url]: https://www.mongodb.com
[mongoose-shield]: https://img.shields.io/badge/mongoose-6.6.5-red
[mongoose-url]: https://mongoosejs.com
[docker-shield]:https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com
[git-shield]:https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-url]: https://git-scm.com

[postman-shield]:https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white
[postman-url]: https://www.postman.com


[twitter-shield]:https://img.shields.io/twitter/follow/molro?style=social
[twitter-url]:https://www.twitter.com/molro
[github-shield]:https://img.shields.io/github/followers/molro?style=social
[github-url]: https://github.com/molro/

[gitMac]:https://git-scm.com/download/mac
[gitLinux]:https://git-scm.com/download/linux
[gitWindows32bit]:https://github.com/git-for-windows/git/releases/download/v2.38.1.windows.1/Git-2.38.1-32-bit.exe 
[gitWindows]:https://git-scm.com/download/win

[pylatestmacos]:https://www.python.org/downloads/release/python-3111/
[pymacos]:https://www.python.org/downloads/macos/

[pylatestwin]:https://www.python.org/downloads/release/python-3111/
[pywin]:https://www.python.org/downloads/windows/

[pygzip]:https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
[pyxz]:https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz

[pywindowsdockermac-url]:https://docs.docker.com/desktop/install/mac-install/

[windowsDocker-url]:https://docs.docker.com/desktop/install/windows-install/#wsl-2-backend
[windowsdektop-url]:https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe

[linuxdocker-url]:https://docs.docker.com/desktop/faqs/linuxfaqs/#what-is-the-difference-between-docker-desktop-for-linux-and-docker-engine
[linuxdockerdesktop-url]:https://docs.docker.com/desktop/install/linux-install/

[license-url]:hhttps://github.com/mouredev/Hello-Python/blob/main/LICENSE