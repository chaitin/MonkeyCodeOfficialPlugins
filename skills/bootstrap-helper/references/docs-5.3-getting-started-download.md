### Install Bootstrap with NuGet

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Install Bootstrap's CSS or Sass and JavaScript for .NET Framework projects using the NuGet package manager. Note that NuGet is primarily for compiled code; consider libman for newer projects managing frontend assets.

```powershell
Install-Package bootstrap
```

```powershell
Install-Package bootstrap.sass
```

--------------------------------

### Install Bootstrap with Bun

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Install Bootstrap version 5.3.8 in your Bun or Node.js powered applications using the Bun CLI.

```shell
bun add bootstrap@5.3.8
```

--------------------------------

### Install Bootstrap with RubyGems

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Install Bootstrap version 5.3.8 in your Ruby applications. It is recommended to use Bundler by adding the gem to your `Gemfile`. Alternatively, you can install the gem directly using the `gem install` command.

```ruby
gem 'bootstrap', '~> 5.3.8'
```

```shell
gem install bootstrap -v 5.3.8
```

--------------------------------

### Install Bootstrap with Yarn

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Install Bootstrap version 5.3.8 in your Node.js applications using the Yarn package manager. For Yarn 2+ (Berry), specific configurations are needed to enable the `node_modules` linker and install dependencies.

```shell
yarn add bootstrap@5.3.8
```

```shell
yarn config set nodeLinker node-modules
touch yarn.lock
yarn install
yarn start
```

--------------------------------

### Install Bootstrap with Composer

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Install and manage Bootstrap's Sass and JavaScript assets in your PHP projects using the Composer package manager.

```shell
composer require twbs/bootstrap:5.3.8
```

--------------------------------

### Install Bootstrap via npm

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Install Bootstrap version 5.3.8 into your Node.js project using npm. This command fetches the package and adds it to your project's dependencies.

```bash
npm install bootstrap@5.3.8
```

--------------------------------

### Generate SRI Hash for Bootstrap JS

Source: https://getbootstrap.com/docs/5.3/getting-started/download

This command-line example demonstrates how to generate a Subresource Integrity (SRI) hash for a JavaScript file using OpenSSL. This is useful for verifying the integrity of files downloaded from CDNs.

```bash
openssl dgst -sha384 -binary bootstrap.min.js | openssl base64 -A
```

--------------------------------

### Import Bootstrap in JavaScript (CommonJS/ES Modules)

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Demonstrates how to import Bootstrap's JavaScript components into your project after installing it via npm. You can either import the entire library or individual plugins.

```javascript
// CommonJS
const bootstrap = require('bootstrap');

// ES Modules
import bootstrap from 'bootstrap';
```

--------------------------------

### Include Bootstrap and Popper via CDN

Source: https://getbootstrap.com/docs/5.3/getting-started/download

If you need to include Bootstrap's JavaScript plugins separately and prefer to manage Popper.js manually, use these script tags. Ensure Popper.js is loaded before Bootstrap's JavaScript.

```html
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.min.js" integrity="sha384-G/EV+4j2dNv+tEPo3++6LCgdCROaejBqfUeNjuKAiuXbjrxilcCdDz6ZAVfHWe1Y" crossorigin="anonymous"></script>
```

--------------------------------

### Include Bootstrap via jsDelivr CDN

Source: https://getbootstrap.com/docs/5.3/getting-started/download

Use these HTML tags to include Bootstrap's compiled CSS and JavaScript directly from the jsDelivr CDN. This method avoids manual downloads and ensures you're using cached versions.

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
```

--------------------------------
