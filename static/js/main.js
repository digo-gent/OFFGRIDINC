import Alpine from 'alpinejs'

import intersect from '@alpinejs/intersect'

import './alpine-directives.js'

import { carousel } from './testimonial-slide.js'

import './infinite-scroll.js'

import  './casestudy.js'

import './intersect-scroll-animation.js'

// Register plugins
Alpine.plugin(intersect)

// Register your custom Alpine component ONCE
Alpine.data('carousel', carousel)

// Assign to window and start Alpine
window.Alpine = Alpine
Alpine.start()
