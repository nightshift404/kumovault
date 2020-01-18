# KumoVault Deployment Guide

## Overview
This document describes containerized and host-level deployment procedures for KumoVault
within KumoSec internal network segments.

## Container Deployment
1. Build the production image:
   ```bash
   docker-compose build
   ```
2. Start the service stack:
   ```bash
   docker-compose up -d
   ```
3. Check container health:
   ```bash
   docker-compose ps
   curl -s http://127.0.0.1:8080/ | jq .
   ```

## Infrastructure Ownership
- Primary Infrastructure Contact: Platform Engineering Team (contact: akr)
- Target Cluster: Internal Services Zone (Zone 2)
