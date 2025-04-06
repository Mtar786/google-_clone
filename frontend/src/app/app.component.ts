import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LocalStorageService } from '@ngx-pwa/local-storage';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-root',
  template: `
    <mat-toolbar color="primary">
      <span>Google+ Clone</span>
      <span class="spacer"></span>
      <ng-container *ngIf="isLoggedIn">
        <button mat-icon-button [matBadge]="unreadNotifications" matBadgeColor="warn" routerLink="/notifications">
          <mat-icon>notifications</mat-icon>
        </button>
        <button mat-icon-button [matMenuTriggerFor]="menu">
          <mat-icon>account_circle</mat-icon>
        </button>
        <mat-menu #menu="matMenu">
          <button mat-menu-item routerLink="/profile">
            <mat-icon>person</mat-icon>
            <span>Profile</span>
          </button>
          <button mat-menu-item routerLink="/circles">
            <mat-icon>group</mat-icon>
            <span>Circles</span>
          </button>
          <button mat-menu-item (click)="logout()">
            <mat-icon>exit_to_app</mat-icon>
            <span>Logout</span>
          </button>
        </mat-menu>
      </ng-container>
      <ng-container *ngIf="!isLoggedIn">
        <button mat-button routerLink="/login">Login</button>
        <button mat-button routerLink="/register">Register</button>
      </ng-container>
    </mat-toolbar>
    <div class="content">
      <router-outlet></router-outlet>
    </div>
  `,
  styles: [`
    .spacer {
      flex: 1 1 auto;
    }
    .content {
      padding: 20px;
      max-width: 1200px;
      margin: 0 auto;
    }
  `]
})
export class AppComponent implements OnInit {
  isLoggedIn = false;
  unreadNotifications = 0;

  constructor(
    private router: Router,
    private localStorage: LocalStorageService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit() {
    this.checkAuthStatus();
  }

  checkAuthStatus() {
    const token = this.localStorage.getItem('access_token');
    this.isLoggedIn = !!token;
  }

  logout() {
    this.localStorage.removeItem('access_token');
    this.isLoggedIn = false;
    this.router.navigate(['/login']);
    this.snackBar.open('Logged out successfully', 'Close', {
      duration: 3000
    });
  }
}