package main

import "testing"

func TestCountZeros(t *testing.T) {
	type args struct {
		A []int
	}
	tests := []struct {
		name string
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			CountZeros(tt.args.A)
		})
	}
}
