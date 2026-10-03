# HackYeah 2026 submission text

## Project name
OrbitGuard Defence

## Problem
Europe's banking, power grids, logistics, crisis response and defence all depend on satellites, and the space around them is getting crowded and contested. About 40,000 objects are tracked in orbit, only about 11,000 of them working satellites, and more than 1.2 million pieces of debris over 1 cm are big enough to destroy one (ESA, 2025). In just six months of 2025, Starlink satellites performed 148,696 manoeuvres to avoid collisions.

Threats are also deliberate now. The 2021 Cosmos 1408 anti-satellite test created more than 1,500 trackable fragments and forced the ISS crew to shelter in their spacecraft. Unknown "inspector" satellites move close to other countries' satellites. GPS jamming around the Baltic disrupts aviation and shipping.

Most governments, civil-protection agencies and smaller operators can't see these threats early. They lack a simple tool that turns orbital data into "what is at risk, when, and what do we do about it".

## Solution
OrbitGuard Defence is a space domain awareness console that tracks 10,000+ objects on a 3D globe. It is built around four steps.

DETECT: every protected satellite (ISS, Tiangong, GPS, Galileo, ICEYE, Sentinel, NOAA, GOES) is automatically checked against the whole catalogue for close approaches in the next 6–24 hours. It also flags unknown objects lingering near geostationary satellites. Alerts are ranked by collision probability, and an AI-written threat brief summarises them for the duty officer.

REDUCE: for any alert, OrbitGuard shows the close-approach geometry and works out the smallest avoidance burn: when to do it, how big it is, how much fuel it takes and how far it lowers the collision risk.

PROTECT: each satellite fleet is linked to the public service that depends on it (crew safety, bank and grid timing, flood mapping, weather), so decision-makers see the impact on people, not just orbits. For crisis response, it predicts the next radar-satellite passes over a city such as Wrocław or Nysa, which matters in floods because radar sees through cloud and works at night.

RESILIENCE: what-if scenarios stress-test the system. One simulates an anti-satellite test that creates a debris cloud, one an inspector satellite approaching a weather satellite, and one the loss of GPS or Galileo satellites over a city. Users see how alerts, threat scores and services change, and how quickly the system detects the new threat.

Benefit: earlier warning, concrete actions, and a clear picture of which services are at risk. It runs in a browser with no installation.

## What's done so far and goal of your project
Before HackYeah: OrbitGuard already had a satellite-tracking engine that loads public orbital data from CelesTrak and calculates positions (SGP4), a 3D globe, a close-approach module and data-driven threat scoring. It's live at orbitguard.live.

During HackYeah we turned it into a defence and resilience console:
(1) a screening engine that checks 120 protected satellites against 10,000+ objects;
(2) a planner for avoidance burns;
(3) a layer that links each fleet to public services;
(4) crisis-imaging pass prediction for Polish cities;
(5) three stress-test scenarios (anti-satellite debris cloud, inspector satellite, GPS/Galileo loss);
(6) an AI threat brief.

Collision probability currently uses a simplified model with assumed tracking error. When live data isn't reachable, the app falls back to a simulated 10,000-object catalogue built on the real orbital shells.

Next goals: use official close-approach warnings from Space-Track and real tracking-error data, add email and SMS alerts and operator accounts, check results against CelesTrak's SOCRATES close-approach reports, and connect with POLSA and the EU Space Surveillance and Tracking network.

## Instructions on how to open project
Open the website link in Chrome, Edge or Firefox. No installation or login needed. To run it locally, download index.html from the repository (or offline/orbitguard-defence-offline.html, which works without internet) and open it in a browser.

Hosted online, the app loads live orbital data from CelesTrak. Without a connection it switches automatically to a simulated 10,000-object catalogue, shown as "Demo catalog" in the top bar.

How to use: Detect shows the alerts (screening runs automatically). Click any alert to open it in Reduce. Resilience runs the scenarios (anti-satellite test, inspector satellite, GNSS loss). Protect shows the services at risk and the next radar passes over a city. Layers highlights constellations such as Starlink or ICEYE. Use 60× or 600× in the top bar to speed up time, and "Watch the flyby" on an alert to see a close approach happen.

## Suggested 2-minute demo
1. Detect: the fleet starts calm (low threat score).
2. Resilience → Run ASAT test: fragments appear and the fleet is re-screened.
3. Detect: open the debris-cloud alert for the crewed station.
4. Reduce: show an avoidance burn on a conjunction alert, then "Watch the flyby".
5. Resilience → GNSS degradation: knock out 70% of GPS over Kraków; GPS alone loses its fix, GPS + Galileo keeps one.

## Sources
- ESA Space Environment Report 2025: https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2025
- SpaceX semi-annual Starlink report (June–Nov 2025), as reported by Grovewire: https://www.altagrove.com/grovewire-news/spacex-148696-starlink-collision-maneuvers-in-6-months-ending-nov-30-continued-issues-with-operators-slipshod-reporting
