#!/usr/bin/env node
// IELTS Learning Design System validator v1
import fs from "node:fs";
import path from "node:path";
const root=process.cwd();
const skip=new Set([".git","node_modules","dist","build",".next"]);
const errors=[],warnings=[];
const mandatory=["DESIGN_SYSTEM.md","AGENTS.md","assets/css/site.css","assets/js/site.js","design-system/index.html","templates/page.html.example","writing/index.html","writing/task1/index.html","writing/task1/README.md"];
const relative=full=>path.relative(root,full).split(path.sep).join("/");
function walk(dir){
 const result=[];
 for(const item of fs.readdirSync(dir,{withFileTypes:true})){
  if(item.isDirectory()&&!skip.has(item.name)) result.push(...walk(path.join(dir,item.name)));
  else if(item.isFile()&&item.name.endsWith(".html"))result.push(path.join(dir,item.name));
 }
 return result;
}
function fail(file,msg){errors.push(relative(file)+": "+msg)}
function check(file){
 const html=fs.readFileSync(file,"utf8"), name=relative(file);
 if(!/<!doctype html>/i.test(html))fail(file,"DOCTYPE missing");
 if(!/<html\b[^>]*\blang=["'][a-z]{2}(?:-[a-z]{2})?["']/i.test(html))fail(file,"lang missing");
 if(!/<meta\b[^>]*\bname=["']viewport["']/i.test(html))fail(file,"viewport missing");
 if(!/<main\b/i.test(html))fail(file,"main missing");
 const h1=(html.match(/<h1(?:\s|>)/gi)||[]).length;
 if(h1!==1)fail(file,"Expected exactly 1 h1, found "+h1);
 if(/<style(?:\s|>)/i.test(html))fail(file,"Inline <style> is forbidden");
 if(/\sstyle\s*=\s*["']/i.test(html))fail(file,"Inline style= is forbidden");
 if(/\son[a-z]+\s*=\s*["']/i.test(html))fail(file,"Inline on* event is forbidden");
 const stylesheets=html.match(/<link\b[^>]*\brel=["']stylesheet["'][^>]*>/gi)||[];
 if(stylesheets.length!==1)fail(file,"Expected exactly one shared CSS <link>, found "+stylesheets.length);
 const css=html.match(/\bhref=["']([^"']*assets\/css\/site\.css)["']/i)?.[1];
 const js=html.match(/\bsrc=["']([^"']*assets\/js\/site\.js)["']/i)?.[1];
 for(const pair of [["CSS",css],["JS",js]]){
  const kind=pair[0],ref=pair[1];
  if(!ref){fail(file,"Missing shared "+kind+" reference");continue;}
  if(/^(https?:|\/)/.test(ref)){fail(file,kind+" asset must use a relative path");continue;}
  const resolved=path.resolve(path.dirname(file),ref);
  if(!resolved.startsWith(root+path.sep))fail(file,kind+" escapes repository");
  else if(!fs.existsSync(resolved))fail(file,kind+" path cannot resolve: "+ref);
 }
 if(!/\bhref=["']\/ielts-learning\/["']/i.test(html))fail(file,"Missing navigation link to Pages root");
 if(name.startsWith("writing/task1/")&&html.includes("compare-section")){
  const count=(html.match(/class=["']compare-section["']/g)||[]).length;
  if(count!==4)fail(file,"Expected 4 compare sections, found "+count);
  if(!html.includes('class="paper original"')||!html.includes('class="paper revised"'))fail(file,"Missing side-by-side original/corrected");
  if(!html.includes('class="diff"'))fail(file,"Missing yellow changed-span marks");
  if(!html.includes('id="revisedEssay"')||!html.includes('id="modelEssay"'))fail(file,"Missing complete essays");
  for(const token of ["hl-logic","hl-trend","hl-degree","hl-data","hl-structure"])
   if(!html.includes(token)) warnings.push(name+" does not mention "+token);
 }
}
for(const filename of mandatory)if(!fs.existsSync(path.join(root,filename)))errors.push("Mandatory file missing: "+filename);
const pages=walk(root);
if(pages.length===0)errors.push("No .html pages found");
for(const file of pages)check(file);
console.log("Design System v1: checked "+pages.length+" HTML pages.");
warnings.forEach(value=>console.warn("WARN "+value));
if(errors.length){
 errors.forEach(value=>console.error("FAIL "+value));
 console.error(errors.length+" violation(s) detected. Check AGENTS.md and DESIGN_SYSTEM.md.");
 process.exitCode=1;
}else console.log("PASS: all machine-checkable design requirements satisfied.");
