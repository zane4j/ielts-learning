#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const issues = [];
function traverse(directory) {
  return fs.readdirSync(directory, {withFileTypes:true}).flatMap(entry=>{
    if(entry.isDirectory()) return entry.name === ".git" || entry.name === "node_modules" ? [] : traverse(path.join(directory,entry.name));
    return entry.isFile() ? [path.join(directory,entry.name)] : [];
  });
}
const all = traverse(root);
const markdown = all.filter(file => file.endsWith(".md"));
const required = ["README.md","speaking/README.md","speaking/part2/people/README.md","speaking/part2/people/IELTS_Part2_Zoe.md","speaking/part2/places/README.md","writing/README.md","writing/task1/README.md"];
for(const file of required) if(!fs.existsSync(path.join(root,file))) issues.push("Missing: "+file);
const pathKey = file => path.relative(root,file).split(path.sep).join("/");
for(const file of markdown) {
  const content = fs.readFileSync(file,"utf8");
  const links = [...content.matchAll(/\[[^\]\n]*\]\(([^)\n]+)\)/g)];
  for(const [, raw] of links) {
    if(/^(?:https?:|mailto:|data:)/i.test(raw)||raw.startsWith("#")) continue;
    const [link,fragment] = raw.replace(/^<|>$/g,"").split("#");
    if(!link) continue;
    const resolved = path.resolve(path.dirname(file),decodeURIComponent(link.split("?")[0]));
    if(!resolved.startsWith(root+path.sep) && resolved!==root){issues.push(pathKey(file)+": link escapes repository "+raw);continue;}
    if(!fs.existsSync(resolved)){issues.push(pathKey(file)+": broken link "+raw);continue;}
    if(fragment?.startsWith("zoe-topic-")) {
      const source=fs.readFileSync(resolved,"utf8");
      if(!source.includes('id="'+fragment+'"')) issues.push(pathKey(file)+": missing Zoe anchor "+fragment);
    }
  }
}
const sourcePath = path.join(root,"speaking/part2/people/IELTS_Part2_Zoe.md");
if(fs.existsSync(sourcePath)){
  const source=fs.readFileSync(sourcePath,"utf8");
  const anchors=[...source.matchAll(/<a id="zoe-topic-(\d{2})"><\/a>/g)].map(x=>x[1]);
  const topics=[...source.matchAll(/^## \d{2}\\\.\s/mg)];
  if(anchors.length!==24||new Set(anchors).size!==24||topics.length!==24) issues.push("Zoe file must keep exactly 24 numbered topics and anchors");
}
const html=all.filter(f=>f.endsWith(".html"));
if(html.length) issues.push("HTML pages found: "+html.map(pathKey).join(", "));
console.log("Markdown check: "+markdown.length+" files and "+html.length+" HTML files");
if(issues.length){for(const issue of issues)console.error("FAIL "+issue);process.exitCode=1;}
else console.log("PASS Markdown links and Zoe index");
