// next.config.js
const nextConfig = {
  experimental: {
    appDir: true,
  },
};
const allowedDomains = require('./app/news/allowedDomains.json');

module.exports = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: allowedDomains, // Allow images from all domains
  },
};


// next.config.js
// module.exports = {
//   images: {
//     domains: ['cdn.mefi.us'], // Add your allowed domains here
//   },
// };
