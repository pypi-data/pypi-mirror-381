import{j as i}from"./index-zOiM5ifH.js";import"./helperFunctions-DLORW2UD.js";import"./hdrFilteringFunctions-Bq3VafDd.js";import"./index-DW22crb7.js";import"./svelte/svelte.js";const r="hdrFilteringPixelShader",e=`#include<helperFunctions>
#include<importanceSampling>
#include<pbrBRDFFunctions>
#include<hdrFilteringFunctions>
uniform float alphaG;uniform samplerCube inputTexture;uniform vec2 vFilteringInfo;uniform float hdrScale;varying vec3 direction;void main() {vec3 color=radiance(alphaG,inputTexture,direction,vFilteringInfo);gl_FragColor=vec4(color*hdrScale,1.0);}`;i.ShadersStore[r]||(i.ShadersStore[r]=e);const c={name:r,shader:e};export{c as hdrFilteringPixelShader};
//# sourceMappingURL=hdrFiltering.fragment-CtiNr_YL.js.map
