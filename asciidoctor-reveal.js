// Load Asciidoctor.js and the reveal.js converter
const asciidoctor = require('@asciidoctor/core')()
const asciidoctorRevealjs = require('@asciidoctor/reveal.js')
asciidoctorRevealjs.register()

// Convert the document 'presentation.adoc' using the reveal.js converter
const options = { safe: 'safe', backend: 'revealjs' }
asciidoctor.convertFile('presentation.adoc', {attributes: {conf : 'bdxio'}, ...options})
