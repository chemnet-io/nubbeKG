class IndexHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <!-- Index Header -->

<header>
  <!-- Nav Bar -->
  <nav id="navbar" class="navbar navbar-light navbar-expand-sm fixed-top">
    <div class="container">
        <a class="navbar-brand title font-weight-lighter" href="./index.html">
           <span class="font-weight-bold">NuBBE[KG]</span>
        </a>
      <!-- Navbar Toggle -->
      <button class="navbar-toggler collapsed ml-auto" type="button" data-toggle="collapse"
              data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
              aria-label="Toggle navigation">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar top-bar"></span>
        <span class="icon-bar middle-bar"></span>
        <span class="icon-bar bottom-bar"></span>
      </button>
      <div class="collapse navbar-collapse text-right" id="navbarNav">
        <ul class="navbar-nav ml-auto flex-nowrap">
          <!-- About -->
          <li class="nav-item active">
            <a class="nav-link" href="./index.html">
              about
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./query/index.html">
              query
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./ontology/index.html">
              ontology
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./dataset/index.html">
              dataset
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./license/index.html">
              license
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./partners/index.html">
              partners

            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./changelog/index.html">
              changelog
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./contact/index.html">
              contact
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="./about/index.html">
              docs
            </a>
          </li>
          <li><button id="light-toggle"></button></li>
        </ul>
      </div>
    </div>
  </nav>
</header>
        `

        //Decide on first render what color theme was chosen and display other theme to tell the user how to change the color theme
        let colorTheme = localStorage.getItem("theme");
        if (colorTheme === "light") {
            // document.getElementById("light-toggle").innerText = "Darkmode"
            document.getElementById("light-toggle").innerHTML = `<img class="icon" src="./assets/img/darkmode.svg">`
        } else {
            document.getElementById("light-toggle").innerHTML = `<img class="icon" src="./assets/img/lightmode.svg">`
        }
    }
}

class SubPageHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <!-- Index Header -->
<header>
  <!-- Nav Bar -->
  <nav id="navbar" class="navbar navbar-light navbar-expand-sm fixed-top">
    <div class="container">
        <a class="navbar-brand title font-weight-lighter" href="../index.html">
           <span class="font-weight-bold">NuBBE[KG]</span>
        </a>
      <!-- Navbar Toggle -->
      <button class="navbar-toggler collapsed ml-auto" type="button" data-toggle="collapse"
              data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
              aria-label="Toggle navigation">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar top-bar"></span>
        <span class="icon-bar middle-bar"></span>
        <span class="icon-bar bottom-bar"></span>
      </button>
      <div class="collapse navbar-collapse text-right" id="navbarNav">
        <ul class="navbar-nav ml-auto flex-nowrap">
          <!-- About -->
          <li id="about-page" class="nav-item">
            <a class="nav-link" href="../index.html">
              about
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li id="query-page" class="nav-item ">
            <a class="nav-link" href="../query/index.html">
              query
            </a>
          </li> 
          <li id="ontology-page" class="nav-item">
            <a class="nav-link" href="../ontology/index.html">
              ontology
            </a>
          </li>
          <li id="dataset-page" class="nav-item ">
            <a class="nav-link" href="../dataset/index.html">
              dataset
            </a>
          </li>
          <li id="license-page" class="nav-item">
            <a class="nav-link" href="../license/index.html">
              license
            </a>
          </li>
          <li id="partners-page" class="nav-item ">
            <a class="nav-link" href="../partners/index.html">
              partners
            </a>
          </li>
          <li id="changelog-page" class="nav-item ">
            <a class="nav-link" href="../changelog/index.html">
              changelog
            </a>
          </li>
          <li id="contact-page" class="nav-item">
            <a class="nav-link" href="../contact/index.html">
              contact
            </a>
          </li>
          <li id="docs-page" class="nav-item">
            <a class="nav-link" href="../about/index.html">
              docs
            </a>
          </li>
          <li>
          <button id="light-toggle"></button>
        </li>
        </ul>
      </div>
    </div>
  </nav>
</header>
        `;

        //Decide on first render what color theme was chosen and display other theme to tell the user how to change the color theme
        let colorTheme = localStorage.getItem("theme");
        if (colorTheme === "light") {
            // document.getElementById("light-toggle").innerText = "Darkmode"
            document.getElementById("light-toggle").innerHTML = `<img class="icon" src="../assets/img/darkmode.svg">`
        } else {
            document.getElementById("light-toggle").innerHTML = `<img class="icon" src="../assets/img/lightmode.svg">`
        }

        //Split url and get sring between two '/'
        let subPageString = window.location.pathname.split(/[//]/)[1];

        //Check url to find out what subpage the user in on
        switch (subPageString) {
            case 'ontology':
                document.getElementById('ontology-page').classList.add('active');
                break;
            case 'query':
                document.getElementById('query-page').classList.add('active');
                break;
            case 'dataset':
                document.getElementById('dataset-page').classList.add('active');
                break;
            case 'license':
                document.getElementById('license-page').classList.add('active');
                break;
            case 'partners':
                document.getElementById('partners-page').classList.add('active');
                break;
            case 'changelog':
                document.getElementById('changelog-page').classList.add('active');
                break;
            case 'contact':
                document.getElementById('contact-page').classList.add('active');
                break;
            case 'ontology':
                document.getElementById('ontology-page').classList.add('active');
                break;
            case 'docs':
                document.getElementById('docs-page').classList.add('active');
                break;
            default: console.log('something went wrong')
        }
    }
}


//Footer
class Footer extends HTMLElement {
    connectedCallback() {
        this.innerHTML =
            `
        <!-- Footer -->
<footer class="fixed-bottom">
    <div class="container mt-0">
        © Copyright 2023 NuBBE[KG]
    </div>
</footer>
      `
    }
}

customElements.define('main-header', IndexHeader);
customElements.define('sub-header', SubPageHeader);
customElements.define('main-footer', Footer);
