// ****************************************************************************
// This file is part of the Integrating Vision Toolkit (IVT).
//
// The IVT is maintained by the Karlsruhe Institute of Technology (KIT)
// (www.kit.edu) in cooperation with the company Keyetech (www.keyetech.de).
//
// Copyright (C) 2012 Karlsruhe Institute of Technology (KIT).
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
//
// 3. Neither the name of the KIT nor the names of its contributors may be
//    used to endorse or promote products derived from this software
//    without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE KIT AND CONTRIBUTORS “AS IS” AND ANY
// EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE KIT OR CONTRIBUTORS BE LIABLE FOR ANY
// DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
// ****************************************************************************
// ****************************************************************************
// Filename:  Structs.h
// Author:    Pedram Azad
// Date:      2004
// ****************************************************************************


#ifndef __STRUCTS_H__
#define __STRUCTS_H__


// ****************************************************************************
// Necessary includes
// ****************************************************************************

#include "Math/Math2d.h"
#include "Math/Math3d.h"
#include "DataStructures/DynamicArrayTemplate.h"

#include <string.h>
#include <vector>



// ****************************************************************************
// Structs
// ****************************************************************************

/*!
	\brief Data structure for the representation of a 2D ellipse.

	The function PrimitivesDrawer::DrawEllipse draws ellipses, given its specification in for of this struct.
 

*/
struct Ellipse2d
{
	/*!
		\brief The center of the ellipse.
	*/
	Vec2d center;
	
	/*!
		\brief The radius in horizontal direction of the ellipse (horizontal refers to when angle = 0).
	*/
	float radius_x;
	
	/*!
		\brief The radius in vertical direction of the ellipse (vertical refers to when angle = 0).
	*/
	float radius_y;
	
	/*!
		\brief The rotiation angle of the ellipse, given in radians.
	
		Note that a positive angle will rotate the ellipse clockwise, as the y-axis of the
		image coordinate system is oriented downward. In the IVt, the rotation angles are consistent for
		all algorithms/functions that involve rotations.
	*/
	float angle;
};

struct ROI
{
	int min_x, min_y, max_x, max_y;
};

struct PointPair2d
{
	Vec2d p1;
	Vec2d p2;
};

struct PointPair3d
{
	Vec3d p1;
	Vec3d p2;
};

struct MyRegion
{
	// constructor
	MyRegion()
	{
		pPixels = 0;
	}

	// copy constructor
	MyRegion(const MyRegion &region)
	{
		nPixels = region.nPixels;

		if (region.pPixels)
		{
			pPixels = new int[nPixels];
			memcpy(pPixels, region.pPixels, nPixels * sizeof(int));
		}
		else
			pPixels = 0;

		Math2d::SetVec(centroid, region.centroid);

		min_x = region.min_x;
		min_y = region.min_y;
		max_x = region.max_x;
		max_y = region.max_y;

		ratio = region.ratio;
	}
	
	// destructor
	~MyRegion()
	{
		if (pPixels)
			delete [] pPixels;
	}

	// assign operator
	MyRegion& operator= (const MyRegion &region)
	{
		nPixels = region.nPixels;

		if (region.pPixels)
		{
			pPixels = new int[nPixels];
			memcpy(pPixels, region.pPixels, nPixels * sizeof(int));
		}
		else
			pPixels = 0;

		Math2d::SetVec(centroid, region.centroid);

		min_x = region.min_x;
		min_y = region.min_y;
		max_x = region.max_x;
		max_y = region.max_y;

		ratio = region.ratio;

		return *this;
	}
	
	// attributes
	int *pPixels;
	int nPixels;
	
	Vec2d centroid;
	
	int min_x;
	int min_y;
	int max_x;
	int max_y;
	
	float ratio;
};


// ****************************************************************************
// Typedefs
// ****************************************************************************

typedef std::vector<MyRegion> RegionList;
typedef CDynamicArrayTemplate<MyRegion> CRegionArray;



#endif /* __STRUCTS_H__ */
