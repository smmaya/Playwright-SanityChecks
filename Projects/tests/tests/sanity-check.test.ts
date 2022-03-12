import { test, expect } from '@playwright/test';

test('1. Login', async ({ page }) => {

  await page.goto('https://www.bing.com/');
  const searchBox = page.locator('input >> nth=0');
  await searchBox.type('Playright');
  await searchBox.waitFor();
  await searchBox.press('Enter', {timeout: 20000});
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'screens/1.png'});

});

test('2. Coś tam...', async ({ page }) => {

  await page.goto('https://www.bing.com/');
  const searchBox = page.locator('input >> nth=0');
  await searchBox.type('Playright');
  await searchBox.waitFor();
  await searchBox.press('Enter', {timeout: 20000});
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'screens/2.png'});

});