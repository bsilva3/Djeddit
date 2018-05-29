import { Component, OnInit } from '@angular/core';
import {Post} from "../post";
import {PostService} from "../post.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-profile-posts-hidden',
  templateUrl: './profile-posts-hidden.component.html',
  styleUrls: ['./profile-posts-hidden.component.css']
})
export class ProfilePostsHiddenComponent implements OnInit {

  posts: Post[];

  constructor(private route: ActivatedRoute, private postService: PostService) { }

  ngOnInit() {
    this.getPosts(this.route.parent.snapshot.paramMap.get("username"));
  }

  getPosts(username: string): void {
    this.postService.getUserPostsHidden(username).subscribe(posts => {this.posts = posts;});
  }

}
