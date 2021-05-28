/**
 * Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
import Emittery = require('emittery');
import type { Config } from '@jest/types';
import type { OnTestFailure, OnTestStart, OnTestSuccess, Test, TestEvents, TestRunnerContext, TestRunnerOptions, TestWatcher } from './types';
export type { Test, OnTestFailure, OnTestStart, OnTestSuccess, TestWatcher, TestRunnerContext, TestRunnerOptions, TestFileEvent, } from './types';
export default class TestRunner {
    private readonly _globalConfig;
    private readonly _context;
    private readonly eventEmitter;
    readonly __PRIVATE_UNSTABLE_API_supportsEventEmitters__: boolean;
    readonly isSerial?: boolean;
    constructor(globalConfig: Config.GlobalConfig, context?: TestRunnerContext);
    runTests(tests: Array<Test>, watcher: TestWatcher, onStart: OnTestStart | undefined, onResult: OnTestSuccess | undefined, onFailure: OnTestFailure | undefined, options: TestRunnerOptions): Promise<void>;
    private _createInBandTestRun;
    private _createParallelTestRun;
    on<Name extends keyof TestEvents>(eventName: Name, listener: (eventData: TestEvents[Name]) => void | Promise<void>): Emittery.UnsubscribeFn;
}
