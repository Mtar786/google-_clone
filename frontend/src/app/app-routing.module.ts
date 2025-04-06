import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './core/guards/auth.guard';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'login',
    loadChildren: () => import('./features/auth/login/login.module').then(m => m.LoginModule)
  },
  {
    path: 'register',
    loadChildren: () => import('./features/auth/register/register.module').then(m => m.RegisterModule)
  },
  {
    path: 'home',
    loadChildren: () => import('./features/home/home.module').then(m => m.HomeModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'profile/:id',
    loadChildren: () => import('./features/profile/profile.module').then(m => m.ProfileModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'post/:id',
    loadChildren: () => import('./features/post/post.module').then(m => m.PostModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'circles',
    loadChildren: () => import('./features/circle/circle.module').then(m => m.CircleModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'notifications',
    loadChildren: () => import('./features/notification/notification.module').then(m => m.NotificationModule),
    canActivate: [AuthGuard]
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }