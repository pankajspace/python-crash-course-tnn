#!/usr/bin/env node

const { execSync } = require('child_process');
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Usage: npm run install-package <package-name>');
    console.log('Examples:');
    console.log('  npm run install-package requests');
    console.log('  npm run install-package "requests pandas numpy"');
    console.log('  npm run install-package django==4.2.0');
    process.exit(1);
}

const packageName = args.join(' ');

try {
    console.log(`Installing ${packageName}...`);

    // Install the package
    execSync(`docker-compose run --rm dev pip install ${packageName}`, {
        stdio: 'inherit'
    });

    // Update requirements.txt
    execSync('docker-compose run --rm dev pip freeze > requirements.txt', {
        stdio: 'inherit'
    });

    console.log(`${packageName} installed and requirements.txt updated!`);
} catch (error) {
    console.error('Error installing package:', error.message);
    process.exit(1);
}